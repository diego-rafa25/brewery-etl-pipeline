import pytest
from etl.aggregate import aggregate_data
import pandas as pd
import os
import shutil

class DummyTI:
    def __init__(self):
        self.store = {}
    def xcom_push(self, key, value):
        self.store[key] = value
    def xcom_pull(self, key, task_ids=None):
        return self.store.get(key)

def test_aggregate_generates_summary(tmp_path):
    """
    Testa se a função aggregate_data gera corretamente a camada Gold a partir dos dados da Silver.

    O teste:
    - Cria um arquivo Parquet simulado representando os dados limpos (camada Silver)
    - Copia esse arquivo para o caminho usado pela função real
    - Executa a função aggregate_data simulando contexto do Airflow
    - Verifica se o arquivo de saída da camada Gold foi gerado
    - Verifica se uma prévia da agregação foi enviada via XCom
    """
    silver_path = tmp_path / "silver"
    silver_path.mkdir()
    df = pd.DataFrame([{"state": "CA", "brewery_type": "micro"}])
    test_file = silver_path / "breweries.parquet"
    df.to_parquet(test_file)

    os.makedirs("data/silver", exist_ok=True)
    shutil.copy(test_file, "data/silver/breweries.parquet")

    context = {"ti": DummyTI()}
    aggregate_data(**context)

    output_file = "data/gold/breweries_summary.parquet"
    assert os.path.exists(output_file)

    preview = context["ti"].xcom_pull("preview_aggregate")
    assert isinstance(preview, list)
    assert len(preview) > 0