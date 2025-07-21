# Data Engineering ETL Project

This project implements a data engineering pipeline based on the Medallion architecture (Bronze → Silver → Gold), using Python, Pandas, Pytest, Docker, and Apache Airflow.  
It consumes public brewery data from the [Open Brewery DB](https://www.openbrewerydb.org), transforms it, and aggregates insights by state and brewery type.

---

## 📦 Technologies Used

- Python 3.12  
- Pandas  
- Apache Airflow  
- Docker & Docker Compose  
- Pytest  
- Open Brewery DB API  

---

## 🗂️ Pipeline Architecture

| Layer      | Description                                          |
|------------|------------------------------------------------------|
| **Bronze** | Raw data extracted from the API and saved as JSON    |
| **Silver** | Cleaned and transformed data saved as Parquet        |
| **Gold**   | Aggregated data grouped by state and brewery type    |

---

## 🚀 How to Run

### ✔️ Prerequisites

- Docker and Docker Compose installed
- A `.env` file in the project root with your credentials (see example below)

### ▶️ Run Locally (Without Airflow)

```bash
python run_local.py
```

---

## 🧪 Unit Tests

Run unit tests for each ETL stage:

```bash
pytest tests/
```

---

## 📊 Test Coverage

To check coverage:

```bash
pytest --cov=etl tests/
```

To generate an HTML report:

```bash
pytest --cov=etl --cov-report=html tests/
start htmlcov/index.html
```

---

## 📧 Email Notification (Optional)

The DAG includes an optional task that sends an email after successful execution using Airflow’s `EmailOperator`.

⚠️ Disabled by default to avoid SMTP configuration dependency.

### How to Enable

- Set up SMTP in `airflow.cfg` (host, port, username, password)  
- Uncomment `notify_success` in `brewery_dag.py`  
- Specify the recipient email in the `to` field  
- Chain the task: `task_aggregate >> notify_success`

🔐 **Important:** Never commit your credentials. Use environment variables or Airflow Connections.

---

## 🐳 Docker Setup

To start Airflow with Docker:

```bash
docker-compose up
```

Make sure the root folder includes a `.env` file:

```dotenv
POSTGRES_USER=airflow
POSTGRES_PASSWORD=your_secure_password
POSTGRES_DB=airflow
AIRFLOW_SECRET_KEY=your_random_secret_key
AIRFLOW_DB_URL=postgresql+psycopg2://airflow:your_secure_password@postgres/airflow
```

📌 Do not commit the `.env` file to the repository.

---

## 📁 Project Structure

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
├── .env (not included)
├── README.md
└── README_pt-br.md
```

---

## 🧹 Cleaning Temporary Files

Remove auxiliary and cache files generated during local testing:

```bash
make clean
```

---

## 👨‍💻 Author

Project created by **Diego Rafael**.  
Feel free to connect on [LinkedIn](https://www.linkedin.com/in/diego-rafael-1057221a0/) or open an issue / pull request to collaborate!

---

## 📄 License

This project is intended for educational and technical exploration only.  
All data is provided publicly by Open Brewery DB.

Licensed under the [MIT License](LICENSE).