import yfinance as yf

# Parameters
ticker = "AAPL"  # Replace with the stock ticker of your choice
start_date = "2020-01-01"
end_date = "2023-12-31"

# Download data
data = yf.download(ticker, start=start_date, end=end_date)

# Save to CSV
data.to_csv(f"{ticker}_stock_data.csv")
print(f"Stock data for {ticker} saved as {ticker}_stock_data.csv.")
