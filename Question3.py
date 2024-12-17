gamestop = yf.Ticker("GME")
gamestop_data = gamestop.history(period="1y")
print(gamestop_data)
