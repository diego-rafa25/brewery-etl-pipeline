import pandas as pd
import json
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def transform_data(**context):
    """
    Transforma os dados da camada bronze e salva como Parquet na camada silver.
    Também loga a amostra recebida via XCom da etapa anterior e envia um preview da transformação.

    Transforms brewery data from the bronze layer and saves it as Parquet in the silver layer.
    Also logs sample received from XCom (extract step), and pushes a preview of transformed data.
    """
    try:
        bronze_path = "data/bronze/breweries.json"
        silver_path = "data/silver"

        if not os.path.exists(bronze_path):
            logging.error(f"[transform] Arquivo {bronze_path} não encontrado")
            raise FileNotFoundError(f"{bronze_path} não existe")

        os.makedirs(silver_path, exist_ok=True)

        with open(bronze_path) as f:
            raw = json.load(f)

        df = pd.DataFrame(raw)

        if df.empty:
            logging.warning("[transform] DataFrame vazio após carregamento")
            raise ValueError("DataFrame vazio — verifique dados de origem")

        # Logar amostra recebida via XCom
        preview = context["ti"].xcom_pull(key="preview_extract", task_ids="extract_data")
        logging.info(f"[transform] Amostra recebida via XCom:\n{json.dumps(preview, indent=2)}")

        # Limpeza de dados
        df = df.dropna(subset=['state', 'brewery_type'])
        df = df[df['state'].str.strip() != '']

        output_file = os.path.join(silver_path, "breweries.parquet")
        df.to_parquet(output_file, index=False, engine="pyarrow")

        logging.info(f"[transform] Dados transformados e salvos em {output_file}")

        # Enviar preview da transformação via XCom (opcional)
        transformed_preview = df.head(5).to_dict(orient="records")
        context["ti"].xcom_push(key="preview_transform", value=transformed_preview)

    except Exception as e:
        logging.error(f"[transform] Erro na transformação: {e}")
        raise