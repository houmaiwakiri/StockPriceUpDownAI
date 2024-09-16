import requests
from bs4 import BeautifulSoup
import pandas as pd

# ページURL
url = "https://nikkeiyosoku.com/stock/all/"

# Webページの内容を取得
response = requests.get(url)
soup = BeautifulSoup(response.content, 'html.parser')

# 銘柄データを格納するリスト
stock_data = []

# 銘柄が格納されているテーブルの行を取得
rows = soup.find_all('tr')

for row in rows:
    cols = row.find_all('td')
    if len(cols) >= 3:  # 必要な情報が揃っている場合
        code = cols[0].text.strip()  # 銘柄コード
        name = cols[1].text.strip()  # 銘柄名
        industry = cols[2].text.strip()  # 業種
        stock_data.append([code, name, industry])

# データをCSVファイルに保存
df = pd.DataFrame(stock_data, columns=['Symbol', 'Name', 'Sector'])
df.to_csv('japan_stock_tickers.csv', index=False, encoding='utf-8-sig')

print(f"{len(stock_data)} 銘柄のデータを取得しました。")
