# 📈 Stock Data Pipeline

This project automates the fetching and storing of daily stock prices using Apache Airflow, Python, and PostgreSQL — all in Docker.

## 🧰 Tech Stack
- Apache Airflow
- Python (pandas, yfinance)
- PostgreSQL
- Docker

## 🚀 How to Run

1. **Install Docker**: https://www.docker.com/products/docker-desktop

2. **Clone or download this project**

3. **Start everything:**

```bash
docker-compose up --build
```

4. **Open Airflow UI**  
Visit: http://localhost:8080  
Login: `admin` / `admin`

5. **Enable the DAG** called `stock_data_pipeline`  
Run it manually to test.

6. **Data is stored** in a PostgreSQL table called `stocks`.

## ✅ What it does

- Pulls daily stock data for AAPL from Yahoo Finance
- Cleans it using pandas
- Inserts it into PostgreSQL
- Runs automatically via Airflow

## ✅ EXTRA

## ✅ plot_stock.py for visualization
- can visualize the shown data
- You might have to install pgAdmin 4 and connect to the local server.
