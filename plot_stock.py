import psycopg2
import pandas as pd
import matplotlib.pyplot as plt

# Connect to your Postgres database
conn = psycopg2.connect(
    host="localhost",
    port=5432,  # add port if needed
    dbname="stockdb",
    user="airflow",
    password="airflow"
)


# Query to get dates and closing prices
query = "SELECT date, close FROM stock_prices ORDER BY date"

# Read data into a pandas DataFrame
df = pd.read_sql(query, conn)
conn.close()

# Plot the closing prices
plt.plot(df['date'], df['close'])
plt.title('AAPL Closing Prices')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.xticks(rotation=45)
plt.tight_layout()  # so labels fit nicely
plt.show()
