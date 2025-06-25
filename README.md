# 📈 Stock Data Pipeline

This project automates the fetching and storing of daily stock prices using Apache Airflow, Python, and PostgreSQL all inside Docker. It also includes ARIMA-based forecasting with data visualization using Matplotlib. 

## 🧰 Tech Stack
- Apache Airflow
- Python (pandas, yfinance, psycopg2, matplotlib, statsmodels)
- PostgreSQL
- Docker Compose

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

- Data Extraction: The DAG in Airflow triggers a Python function that fetches the last 30 days of AAPL stock data using the yfinance API.

- Data Wrangling: The data is cleaned and parsed into appropriate types (date, float, integer).

- Database Storage: Cleaned records are inserted into a PostgreSQL table named stock_prices. Duplicate dates are skipped via a conflict check.

- Forecasting & Visualization: A separate script reads the data from PostgreSQL, fits an ARIMA model, and visualizes both historical and predicted prices.

## 📈 How to run plot_stock.py for visualization
- bash: python plot_stock.py

Example from the 25/06/2025
![image](https://github.com/user-attachments/assets/5a23ce28-ac96-468a-8448-63bb2c1a348f)
