# 📊 Projeto de Engenharia de Dados — Brewery ETL Pipeline

Este projeto implementa um pipeline de engenharia de dados baseado na arquitetura Medallion (Bronze → Silver → Gold), utilizando Python, Pandas, Pytest, Docker e Apache Airflow.  
Ele consome dados públicos da [Open Brewery DB](https://www.openbrewerydb.org), transforma e agrega informações sobre cervejarias dos Estados Unidos.

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

O pipeline segue o padrão Medallion:

| Camada   | Descrição                                                |
|----------|-----------------------------------------------------------|
| **Bronze** | Dados brutos extraídos da API e salvos em JSON           |
| **Silver** | Dados transformados e limpos, salvos em formato Parquet  |
| **Gold**   | Dados agregados por estado e tipo de cervejaria          |

---

## 🚀 Como executar

### ✔️ Pré-requisitos

- Docker e Docker Compose instalados

### ▶️ Execução local (sem Airflow)

Execute o pipeline localmente com:

```bash
python run_local.py
```

---

## 🧪 Testes unitários

O projeto inclui testes com `pytest` para cada etapa do pipeline ETL:

```bash
pytest tests/
```

---

## 📊 Cobertura de testes

Para validar a cobertura de código:

```bash
pytest --cov=etl tests/
```

Para gerar um relatório visual em HTML:

```bash
pytest --cov=etl --cov-report=html tests/
start htmlcov/index.html
```

---

## 📧 Notificações por e-mail (opcional)

O pipeline possui uma task opcional que envia um e-mail ao final da execução da DAG utilizando o `EmailOperator` do Airflow.

⚠️ Essa funcionalidade está desabilitada por padrão para evitar dependência de configuração SMTP.

### Como ativar

- Configure as credenciais SMTP no arquivo `airflow.cfg` (host, porta, usuário, senha)  
- Descomente a task `notify_success` no arquivo `brewery_dag.py`  
- Preencha o e-mail destinatário no campo `to`  
- Encadeie ao final da DAG: `task_aggregate >> notify_success`

🔐 **Importante**: Nunca exponha suas credenciais diretamente no repositório público.  
Utilize variáveis de ambiente ou conexões via Airflow.

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
├── README.md
└── README_pt-br.md
```

---

## 🧹 Limpeza de arquivos temporários

Para remover arquivos auxiliares e caches gerados durante testes ou execução local:

```bash
make clean
```

---

## 👨‍💻 Autor

Projeto desenvolvido por **Diego Rafael**.  
Fique à vontade para entrar em contato via [LinkedIn](https://www.linkedin.com/in/diego-rafael-1057221a0/) ou sugerir melhorias por *pull request*!

---

## 🍻 Licença

Este projeto é destinado exclusivamente a fins educacionais e técnicos.  
Os dados utilizados são públicos e fornecidos pela Open Brewery DB.