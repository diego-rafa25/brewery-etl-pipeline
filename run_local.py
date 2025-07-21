"""
Execução Local do Pipeline ETL | Local ETL Pipeline Execution

Este script simula o fluxo completo de extração, transformação e agregação
de dados da Open Brewery DB, utilizando objetos simulados para o Airflow (XCom).

This script simulates the complete data flow of extraction, transformation,
and aggregation from the Open Brewery DB using a dummy Airflow context (XCom).
"""

from etl.extract import extract_data
from etl.transform import transform_data
from etl.aggregate import aggregate_data
import logging

# Configuração de logging local | Local logging setup
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class DummyTI:
    """
    🧩 Simulador de TaskInstance (XCom) | Simulates Airflow TaskInstance (XCom)

    Implementa xcom_push e xcom_pull para permitir passagem de dados entre etapas
    durante testes locais do pipeline.

    Implements xcom_push and xcom_pull to allow data sharing between steps
    during local pipeline testing.
    """
    def __init__(self):
        self.store = {}

    def xcom_push(self, key, value):
        self.store[key] = value

    def xcom_pull(self, key, task_ids=None):
        return self.store.get(key)

# Executar pipeline completo | Run full pipeline
context = {"ti": DummyTI()}

extract_data(**context)
transform_data(**context)
aggregate_data(**context)