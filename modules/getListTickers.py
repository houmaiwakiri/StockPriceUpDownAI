import requests
from bs4 import BeautifulSoup
import pandas as pd
from pathlib import Path

def fetch_stock_data(url):
  stock_data = []

  # Webページの内容を取得
  try:
    response = requests.get(url)
    response.raise_for_status()  # HTTPエラーが発生した場合に例外を投げる
  except requests.exceptions.RequestException as e:
    print(f"Error fetching data: {e}")
    return []

  soup = BeautifulSoup(response.content, 'html.parser')
  rows = soup.find_all('tr')

  for row in rows:
    cols = row.find_all('td')
    if len(cols) >= 3:  # 必要な情報が揃っている場合
      # 列名を変数に割り当てる
      symbol = cols[0].text.strip()  # 銘柄コード
      name = cols[1].text.strip()    # 銘柄名
      sector = cols[2].text.strip()  # 業種

      # データをリストとして追加
      stock_data.append({
        'Symbol': symbol,
        'Name': name,
        'Sector': sector,
      })
  return stock_data

def save_stock_data(stock_data, output_file):
  # データをCSVに保存
  df = pd.DataFrame(stock_data)  # 列名が辞書のキーになるので明示的に指定しなくてもOK
  df.to_csv(output_file, index=False, encoding='utf-8-sig')
  print(f"{len(stock_data)} rows processed and saved to {output_file}")

def main():
  # outputディレクトリを作成（存在しない場合）
  current_dir = Path(__file__).resolve().parent.parent
  output_dir = current_dir / "output"
  output_dir.mkdir(exist_ok=True)

  stock_tickers_file = output_dir / 'japan_stock_tickers.csv'
  url = "https://nikkeiyosoku.com/stock/all/"

  # 株データの取得
  stock_data = fetch_stock_data(url)
  
  # データを保存する
  if stock_data:
    save_stock_data(stock_data, stock_tickers_file)

if __name__ == "__main__":
  main()
