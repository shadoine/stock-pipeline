from airflow import DAG
from airflow.operators.python import PythonOperator
from datetime import datetime, timedelta
import yfinance as yf
import psycopg2
import pandas as pd

default_args = {
    'owner': 'airflow',
    'depends_on_past': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
}

def fetch_and_store(**kwargs):
    # Download stock data for a given ticker (Apple in here, but this can be replaced by any ticker symbol)
    ticker = "AAPL"
    data = yf.download(ticker, period="1d")

    # Connect to your PostgreSQL database
    conn = psycopg2.connect(
        host="postgres",
        dbname="stockdb",
        user="airflow",
        password="airflow",
        port=5432
    )
    cursor = conn.cursor()

    # Create table if not exists
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS stock_prices (
            date DATE PRIMARY KEY,
            open FLOAT,
            high FLOAT,
            low FLOAT,
            close FLOAT,
            volume BIGINT
        );
    """)

    # Insert each row of data
    for index, row in data.iterrows():
        date = pd.to_datetime(index).date()
        open_price = float(row['Open'])
        high_price = float(row['High'])
        low_price = float(row['Low'])
        close_price = float(row['Close'])
        volume = int(row['Volume'])

        cursor.execute("""
            INSERT INTO stock_prices (date, open, high, low, close, volume) 
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (date) DO NOTHING;
        """, (date, open_price, high_price, low_price, close_price, volume))

    conn.commit()
    cursor.close()
    conn.close()

with DAG(
    'stock_data_pipeline',
    default_args=default_args,
    description='Fetch stock data and store in Postgres',
    schedule_interval=timedelta(days=1),
    start_date=datetime(2025, 6, 1),
    catchup=False,
    tags=['stocks'],
) as dag:

    fetch_store_task = PythonOperator(
        task_id='fetch_and_store',
        python_callable=fetch_and_store,
        provide_context=True
    )
