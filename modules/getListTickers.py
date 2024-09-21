import requests
from bs4 import BeautifulSoup
import pandas as pd

#######
# 定義
#######
stock_tickers_file = 'japan_stock_tickers.csv'
url = "https://nikkeiyosoku.com/stock/all/"
stock_data = []

# Webページの内容を取得
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')
rows = soup.find_all('tr')

# ループ
for row in rows:
  cols = row.find_all('td')
  if len(cols) >= 3:  # 必要な情報が揃っている場合
    code = cols[0].text.strip()  # 銘柄コード
    name = cols[1].text.strip()  # 銘柄名
    Sector = cols[2].text.strip()  # 業種
    stock_data.append([code, name, Sector])

# データをCSVに保存
df = pd.DataFrame(stock_data, columns=['Symbol', 'Name', 'Sector'])
df.to_csv(stock_tickers_file, index=False, encoding='utf-8-sig')

print(f"{len(stock_data)} finish!")
