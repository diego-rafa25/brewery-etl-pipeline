import requests
import json
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def extract_data(**context):
    """
    Extrai dados da API Open Brewery DB e salva como JSON na camada bronze.
    Também envia uma amostra para o XCom do Airflow.

    Extracts data from the Open Brewery DB API and stores the content in JSON format (bronze layer).
    Also pushes a sample to Airflow’s XCom for downstream inspection.
    """
    url = "https://api.openbrewerydb.org/v1/breweries"
    headers = {"User-Agent": "brewery-etl-pipeline"}

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code == 200 and response.content:
            logging.info(f"[extract] Tamanho da resposta da API: {len(response.content)} bytes")

            try:
                data = response.json()

                # Validação básica da estrutura da resposta
                if not isinstance(data, list) or not all("name" in item for item in data):
                    raise ValueError("Resposta inesperada da API — estrutura inválida")

                os.makedirs("data/bronze", exist_ok=True)

                with open("data/bronze/breweries.json", "w") as f:
                    json.dump(data, f, indent=2)

                logging.info("[extract] Dados salvos em data/bronze/breweries.json")

                preview = data[:5]
                logging.info(f"[extract] Prévia dos dados extraídos:\n{json.dumps(preview, indent=2)}")
                context["ti"].xcom_push(key="preview_extract", value=preview)

            except ValueError as e:
                logging.error(f"[extract] Erro ao decodificar ou validar JSON: {e}")
                raise

        else:
            msg = f"Falha na requisição: status {response.status_code}"
            logging.error(f"[extract] {msg}")
            raise RuntimeError(msg)

    except Exception as e:
        logging.error(f"[extract] Erro ao consumir API: {e}")
        raise