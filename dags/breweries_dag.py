"""
DAG: Brewery ETL Pipeline | Pipeline de ETL de Cervejarias

Esta DAG extrai dados da Open Brewery DB, aplica transformação e gera uma agregação por estado e tipo.
Pode ser estendida com uma task de notificação por e-mail (opcional).

This DAG extracts data from the Open Brewery DB, applies transformation, and creates a summary by state and type.
It can be extended with an optional email notification task.
"""

from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime
from etl.extract import extract_data
from etl.transform import transform_data
from etl.aggregate import aggregate_data

#  Definição da DAG e frequência
with DAG(
    dag_id='brewery_etl_pipeline',
    start_date=datetime(2024, 1, 1),
    schedule_interval='@daily',
    catchup=False,
    description='ETL pipeline for Open Brewery DB',
    tags=['brewery', 'ETL', 'data-pipeline'],
) as dag:

    # Task de extração
    task_extract = PythonOperator(
        task_id='extract_data',
        python_callable=extract_data
    )

    # Task de transformação
    task_transform = PythonOperator(
        task_id='transform_data',
        python_callable=transform_data
    )

    # Task de agregação
    task_aggregate = PythonOperator(
        task_id='aggregate_data',
        python_callable=aggregate_data
    )

    # Encadeamento das tasks
    task_extract >> task_transform >> task_aggregate

    # Task opcional de notificação (desabilitada)
    # Para ativar, remova os comentários e configure o SMTP via Airflow

    # from airflow.operators.email import EmailOperator
    # notify_success = EmailOperator(
    #     task_id='notify_success',
    #     to='seu@email.com',  # Melhor definir via Variable ou Connection
    #     subject='Brewery ETL finalizado com sucesso',
    #     html_content="""
    #         <h3>Pipeline Concluído</h3>
    #         <p>A DAG <strong>brewery_etl_pipeline</strong> foi executada com sucesso.</p>
    #     """,
    # )

    # task_aggregate >> notify_success