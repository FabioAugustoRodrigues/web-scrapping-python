import requests
from bs4 import BeautifulSoup
import pandas as pd

url = "https://quotes.toscrape.com"
response = requests.get(url)

if response.status_code == 200:
    soup = BeautifulSoup(response.content, "html.parser")

    data = []
    for quote in soup.find_all('div', class_='quote'):
        text = quote.find('span', class_='text').get_text(strip=True)
        author = quote.find('small', class_='author').get_text(strip=True)
        data.append({'Quote': text, 'Author': author})

    df = pd.DataFrame(data)
    print(df)
else:
    print("Failed to retrieve the webpage.")
