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

The pipeline follows the Medallion pattern:

| Layer      | Description                                          |
|------------|------------------------------------------------------|
| **Bronze** | Raw data extracted from the API and saved as JSON    |
| **Silver** | Cleaned and transformed data saved as Parquet        |
| **Gold**   | Aggregated data grouped by state and brewery type    |

---

## 🚀 How to Run

### ✔️ Prerequisites

- Docker and Docker Compose installed

### ▶️ Run Locally (Without Airflow)

```bash
python run_local.py
```

---

## 🧪 Unit Tests

The project includes unit tests for each ETL stage using `pytest`:

```bash
pytest tests/
```

---

## 📊 Test Coverage

To check coverage:

```bash
pytest --cov=etl tests/
```

To generate a visual HTML report:

```bash
pytest --cov=etl --cov-report=html tests/
start htmlcov/index.html
```

---

## 📧 Email Notification (Optional)

The DAG includes an optional task that sends an email upon successful completion using Airflow’s `EmailOperator`.

⚠️ This feature is disabled by default to avoid SMTP configuration dependency.

### How to Enable

- Set up SMTP details in `airflow.cfg` (host, port, username, password)  
- Uncomment the `notify_success` task in `brewery_dag.py`  
- Add your recipient email to the `to` field  
- Chain the task in the DAG: `task_aggregate >> notify_success`

🔐 **Important**: Never store email credentials in a public repository.  
Use Airflow's environment variables or secure Connections to protect sensitive data.

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
├── README.md
└── README_pt-br.md
```

---

## 🧹 Cleaning Temporary Files

To remove auxiliary and cache files generated during local testing:

```bash
make clean
```

---

## 👨‍💻 Author

Project created by **Diego Rafael**.  
Feel free to connect via [LinkedIn](https://www.linkedin.com/in/diego-rafael-1057221a0/) or open an issue / pull request to collaborate!

---

## 📄 License

This project is for educational and technical exploration only.  
All data used is publicly provided by Open Brewery DB.
