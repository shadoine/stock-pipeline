import pandas as pd
import matplotlib.pyplot as plt

# Sample data (similar to what would be pulled from the database)
data = {
    'date': pd.date_range(start='2025-05-29', periods=7, freq='D'),
    'close': [189.44, 190.18, 188.95, 191.32, 192.10, 190.76, 193.00]
}

# Create DataFrame
df = pd.DataFrame(data)

# Plot the closing prices
plt.figure(figsize=(10, 5))
plt.plot(df['date'], df['close'], marker='o', linestyle='-', color='blue')

# Styling
plt.title('AAPL Closing Prices (Sample Data)', fontsize=14)
plt.xlabel('Date', fontsize=12)
plt.ylabel('Close Price (USD)', fontsize=12)
plt.grid(True)
plt.xticks(rotation=45)
plt.tight_layout()  # So labels don't get cut off

# Show plot
plt.show()
