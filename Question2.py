import requests
from bs4 import BeautifulSoup

url = 'https://finance.yahoo.com/quote/TSLA/financials'
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

# Find the table containing the revenue data
revenue_table = soup.find('table', {'data-test': 'fin-row'})
rows = revenue_table.find_all('tr')

for row in rows:
    cols = row.find_all('td')
    for col in cols:
        print(col.text)
