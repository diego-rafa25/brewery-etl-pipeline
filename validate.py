"""
Validação das Camadas do Pipeline ETL | ETL Pipeline Layer Validation

Este script verifica os arquivos gerados nas camadas bronze, silver e gold,
informando estrutura, quantidade de registros e exemplos de conteúdo.

This script inspects the output files from bronze, silver, and gold layers,
reporting structure, record counts, and sample content.
"""

import os
import json
import pandas as pd
import logging

# Configuração básica de logging
logging.basicConfig(level=logging.INFO, format="%(levelname)s: %(message)s")

def validate_bronze():
    """
    Verifica se o arquivo JSON da camada bronze existe e quantos registros possui.

    Checks if the bronze layer JSON file exists and reports the number of records.
    """
    path = "data/bronze/breweries.json"
    if not os.path.exists(path):
        logging.error(" Bronze file not found.")
        return
    with open(path) as f:
        data = json.load(f)
    logging.info(f" [bronze] {len(data)} records extracted from JSON.")

def validate_silver():
    """
    Valida a estrutura do Parquet da camada silver, colunas presentes e estados únicos.

    Validates the structure of the silver layer Parquet file, columns and unique states.
    """
    path = "data/silver/breweries.parquet"
    if not os.path.exists(path):
        logging.error(" Silver file not found.")
        return
    df = pd.read_parquet(path)
    logging.info(f" [silver] {df.shape[0]} records, {df.shape[1]} columns.")
    logging.info(f" [silver] Columns: {df.columns.tolist()}")
    logging.info(f" [silver] Unique states: {df['state'].nunique()}")

def validate_gold():
    """
    Verifica a agregação final na camada gold e mostra uma amostra de agrupamentos.

    Validates final aggregation in the gold layer and shows a sample of grouped data.
    """
    path = "data/gold/breweries_summary.parquet"
    if not os.path.exists(path):
        logging.error(" Gold file not found.")
        return
    df = pd.read_parquet(path)
    logging.info(f" [gold] {df.shape[0]} aggregated rows.")
    logging.info(" [gold] Example output:")
    logging.info(f"\n{df.head().to_string(index=False)}")

if __name__ == "__main__":
    logging.info(" Starting ETL validation...\n")
    validate_bronze()
    validate_silver()
    validate_gold()