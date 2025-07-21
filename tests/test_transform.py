import pytest
from etl.transform import transform_data
import json
import os
import shutil

class DummyTI:
    def __init__(self):
        self.store = {}
    def xcom_push(self, key, value):
        self.store[key] = value
    def xcom_pull(self, key, task_ids=None):
        return self.store.get(key)

def test_transform_creates_parquet(tmp_path):
    """
    Testa se a função transform_data gera corretamente a camada Silver a partir da Bronze.

    O teste:
    - Cria um arquivo JSON com dados simulados da camada Bronze
    - Copia esse arquivo para o caminho utilizado pela função real
    - Executa a função transform_data simulando o ambiente do Airflow
    - Verifica se o arquivo Parquet da camada Silver foi criado com sucesso
    """
    raw_data = [{"name": "Test Brewery", "state": "CA", "brewery_type": "micro"}]
    bronze_path = tmp_path / "bronze"
    bronze_path.mkdir()
    test_file = bronze_path / "breweries.json"

    with open(test_file, "w") as f:
        json.dump(raw_data, f)

    os.makedirs("data/bronze", exist_ok=True)
    shutil.copy(test_file, "data/bronze/breweries.json")

    context = {"ti": DummyTI()}
    transform_data(**context)

    output_file = "data/silver/breweries.parquet"
    assert os.path.exists(output_file)