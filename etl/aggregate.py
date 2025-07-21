import pandas as pd
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def aggregate_data(**context):
    """
    Realiza agregação por estado e tipo de cervejaria, gera Parquet na camada Gold
    e envia uma amostra agregada via XCom para monitoramento.

    Aggregates brewery data by state and type into a summary Parquet file
    and pushes a preview sample to Airflow's XCom.
    """
    try:
        silver_file = "data/silver/breweries.parquet"
        gold_path = "data/gold"

        if not os.path.exists(silver_file):
            logging.error(f"[aggregate] Arquivo {silver_file} não encontrado")
            raise FileNotFoundError(f"{silver_file} não existe")

        df = pd.read_parquet(silver_file)

        if df.empty:
            logging.warning("[aggregate] DataFrame vazio — nada para agregar")
            raise ValueError("DataFrame da camada Silver está vazio")

        if not {'state', 'brewery_type'}.issubset(df.columns):
            raise ValueError("Colunas esperadas ausentes no DataFrame")

        agg = df.groupby(['state', 'brewery_type']).size().reset_index(name='count')

        os.makedirs(gold_path, exist_ok=True)
        output_file = os.path.join(gold_path, "breweries_summary.parquet")
        agg.to_parquet(output_file, index=False, engine="pyarrow")

        logging.info(f"[aggregate] Agregações salvas em {output_file}")

        preview = agg.head(5).to_dict(orient="records")
        context["ti"].xcom_push(key="preview_aggregate", value=preview)
        logging.info(f"[aggregate] Amostra enviada via XCom:\n{preview}")

    except Exception as e:
        logging.error(f"[aggregate] Erro na agregação: {e}")
        raise