import yfinance as yf
import pandas as pd
import time

# 1. 銘柄リストをCSVから読み込む
# CSVには銘柄コードがリストされている（例：7203, 6758など）
ticker_list = pd.read_csv('japan_stock_tickers.csv')  # 銘柄コードリストのCSVファイル

# 取得した株価データを保存するためのリスト
all_stock_data = []

# 2. 各銘柄について株価を取得し、日次のデータを保存
for ticker in ticker_list['Symbol']:
    try:
        # 銘柄コードに ".T" を追加（日本の株式市場を示す）
        ticker_with_t = str(ticker) + ".T"
        
        # 1年間のデータを取得（1日単位）
        stock_data = yf.Ticker(ticker_with_t).history(period='1d')  # 1日分のデータを取得
        stock_data['Ticker'] = ticker_with_t  # 銘柄コードをデータに追加
        all_stock_data.append(stock_data)
        print(f"Fetched data for {ticker_with_t}")

        # Yahoo Financeに対して大量リクエストを送らないように適度に間隔を開ける
        time.sleep(1)  # 2秒待つ

    except Exception as e:
        print(f"Failed to fetch data for {ticker_with_t}: {e}")

# 3. すべてのデータを1つのデータフレームにまとめる
if len(all_stock_data) > 0:
    combined_data = pd.concat(all_stock_data)
    
    # 4. データをCSVファイルに保存
    combined_data.to_csv('japan_stock_data.csv')
    print("All stock data saved to japan_stock_data.csv")
else:
    print("No stock data was fetched.")
