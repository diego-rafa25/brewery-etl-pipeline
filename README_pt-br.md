# Projeto de Engenharia de Dados

Este projeto implementa um pipeline de engenharia de dados baseado na arquitetura Medallion (Bronze → Silver → Gold), utilizando Python, Pandas, Pytest, Docker e Apache Airflow.  
Ele consome dados públicos da [Open Brewery DB](https://www.openbrewerydb.org), transforma e agrega informações por estado e tipo de cervejaria nos EUA.

---

## 📦 Tecnologias utilizadas

- Python 3.12  
- Pandas  
- Apache Airflow  
- Docker & Docker Compose  
- Pytest  
- Open Brewery DB API  

---

## 🗂️ Arquitetura do pipeline

| Camada   | Descrição                                                |
|----------|----------------------------------------------------------|
| **Bronze** | Dados brutos extraídos da API e salvos como JSON         |
| **Silver** | Dados limpos e transformados, salvos em formato Parquet |
| **Gold**   | Dados agregados por estado e tipo de cervejaria         |

---

## 🚀 Como executar

### ✔️ Pré-requisitos

- Docker e Docker Compose instalados  
- Um arquivo `.env` na raiz do projeto com suas variáveis

### ▶️ Execução local (sem Airflow)

```bash
python run_local.py
```

---

## 🧪 Testes unitários

Execute os testes com `pytest`:

```bash
pytest tests/
```

---

## 📊 Cobertura de testes

Verifique cobertura com:

```bash
pytest --cov=etl tests/
```

Gere um relatório visual em HTML:

```bash
pytest --cov=etl --cov-report=html tests/
start htmlcov/index.html
```

---

## 📧 Notificações por e-mail (opcional)

A DAG possui uma tarefa opcional que envia e-mail após a execução, usando o `EmailOperator` do Airflow.

⚠️ Desabilitada por padrão para evitar dependência de SMTP.

### Como ativar

- Configure SMTP no `airflow.cfg` (host, porta, usuário e senha)  
- Descomente a task `notify_success` em `brewery_dag.py`  
- Defina o e-mail de destino no campo `to`  
- Encadeie a tarefa: `task_aggregate >> notify_success`

🔐 **Importante:** Nunca exponha credenciais no repositório.  
Utilize variáveis de ambiente ou conexões seguras do Airflow.

---

## 🐳 Setup com Docker

Para iniciar o Airflow com Docker:

```bash
docker-compose up
```

Crie um arquivo `.env` na raiz contendo:

```dotenv
POSTGRES_USER=airflow
POSTGRES_PASSWORD=sua_senha_segura
POSTGRES_DB=airflow
AIRFLOW_SECRET_KEY=sua_chave_aleatoria
AIRFLOW_DB_URL=postgresql+psycopg2://airflow:sua_senha_segura@postgres/airflow
```

📌 Não versionar o `.env` no GitHub.

---

## 📁 Estrutura do projeto

```
brewery-pipeline/
├── etl/
│   ├── extract.py
│   ├── transform.py
│   └── aggregate.py
├── tests/
│   ├── test_extract.py
│   ├── test_transform.py
│   └── test_aggregate.py
├── run_local.py
├── validate.py
├── brewery_dag.py
├── docker-compose.yml
├── .env (não incluído)
├── README.md
└── README_pt-br.md
```

---

## 🧹 Limpeza de arquivos temporários

Para remover caches e arquivos auxiliares após testes:

```bash
make clean
```

---

## 👨‍💻 Autor

Projeto desenvolvido por **Diego Rafael**.  
Fique à vontade para entrar em contato pelo [LinkedIn](https://www.linkedin.com/in/diego-rafael-1057221a0/) ou sugerir melhorias via *pull request*!

---

## 🍻 Licença

Este projeto é destinado exclusivamente a fins educacionais e técnicos.  
Os dados utilizados são públicos e fornecidos pela Open Brewery DB.

Licenciado sob a [MIT License](LICENSE).