import yfinance as yf
tesla = yf.Ticker("TSLA")
tesla_data = tesla.history(period="1y")
print(tesla_data)
