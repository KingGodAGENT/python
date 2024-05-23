import yfinance

t = yfinance.Ticker("NVDA")
stock = t.history(period="1d")
current = stock["Close"].iloc[-1]
print(current)