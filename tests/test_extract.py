import pytest
from etl.extract import extract_data

class DummyTI:
    def __init__(self):
        self.store = {}
    def xcom_push(self, key, value):
        self.store[key] = value
    def xcom_pull(self, key, task_ids=None):
        return self.store.get(key)

def test_extract_pushes_preview():
    """
    Testa se a função extract_data insere corretamente uma prévia dos dados no XCom.
    
    Simula o comportamento do Airflow usando um DummyTI, executa a função extract_data e verifica:
    - Se o preview está presente no XCom
    - Se o preview é uma lista
    - Se a lista contém ao menos um item
    """
    context = {"ti": DummyTI()}
    extract_data(**context)
    preview = context["ti"].xcom_pull("preview_extract")
    assert isinstance(preview, list)
    assert len(preview) > 0