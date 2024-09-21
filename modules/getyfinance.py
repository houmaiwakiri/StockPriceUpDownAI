import yfinance as yf
import pandas as pd
import os
import time

#################
# 定義
#################
stock_list_file = 'japan_stock_tickers.csv'
stock_data_file = 'japan_stock_data.csv'

current_dir = os.path.dirname(__file__)

#################################################################
# 1. 銘柄リストをCSVから読み込む関数
#################################################################
def load_stock_list():
  csv_file_path = os.path.join(current_dir, '..', 'output', stock_list_file)
  csv_file_path = os.path.abspath(csv_file_path)

  try:
    ticker_list = pd.read_csv(csv_file_path)
    print(f"Loaded {len(ticker_list)} tickers from {stock_list_file}")
    return ticker_list
  except Exception as e:
    print(f"Failed to load stock list: {e}")
    return None

##################################################
# 2. 株価を取得し、データフレームに追加する関数
##################################################
def fetch_stock_data(ticker_list):
  all_stock_data = []
  for ticker in ticker_list['Symbol']:
    try:
      # 銘柄コードに ".T" を追加（日本の株式市場を示す）
      ticker_with_t = str(ticker) + ".T"

      # 1年間のデータを取得（1日単位）
      stock_data = yf.Ticker(ticker_with_t).history(period='1d')  # 1日分のデータを取得
      stock_data['Ticker'] = ticker_with_t  # 銘柄コードをデータに追加
      all_stock_data.append(stock_data)
      print(f"Fetched data for {ticker_with_t}")

      # Yahoo Financeへの負荷軽減
      time.sleep(0.1) 

    except Exception as e:
      print(f"Failed to fetch data for {ticker_with_t}: {e}")
    
  return all_stock_data

##################################################
# 3. 取得したデータをCSVに保存する関数
##################################################
def save_stock_data(all_stock_data):
  if len(all_stock_data) > 0:
    combined_data = pd.concat(all_stock_data)
    combined_data.to_csv(stock_data_file)
    print(f"All stock data saved to {stock_data_file}")
  else:
    print("No stock data was fetched.")

##################################################
# メイン処理
##################################################
def main():
  # 1. 銘柄リストを読み込む
  ticker_list = load_stock_list()
  
  if ticker_list is not None:
    # 2. 株価を取得する
    all_stock_data = fetch_stock_data(ticker_list)
    
    # 3. データを保存する
    save_stock_data(all_stock_data)

if __name__ == "__main__":
    main()
