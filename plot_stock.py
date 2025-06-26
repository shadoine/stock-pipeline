import psycopg2
import pandas as pd
import matplotlib.pyplot as plt
from statsmodels.tsa.arima.model import ARIMA
from datetime import timedelta

# Connect to PostgreSQL
conn = psycopg2.connect(
    host="localhost",
    port=5433,
    dbname="stockdb",
    user="airflow",
    password="airflow"
)

# Load historical stock closing prices
query = "SELECT date, close FROM stock_prices ORDER BY date"
df = pd.read_sql(query, conn)
conn.close()

# Ensure the date column is datetime and set as index
df['date'] = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

# Fit ARIMA model
model = ARIMA(df['close'], order=(5, 1, 0))  # ARIMA(p,d,q)
model_fit = model.fit()

# Forecast next 5 days
forecast_steps = 5
forecast = model_fit.forecast(steps=forecast_steps)

# Create forecast dates
last_date = df.index[-1]
forecast_dates = [last_date + timedelta(days=i) for i in range(1, forecast_steps + 1)]

# Plot the original and forecasted values
plt.figure(figsize=(10, 6))
plt.plot(df.index, df['close'], label='Historical Closing Prices')
plt.plot(forecast_dates, forecast, label='Forecast', color='red', marker='o')
plt.title('AAPL Closing Price Forecast with ARIMA')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.legend()
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
