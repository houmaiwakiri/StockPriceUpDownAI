# 株価予測

## 処理(main.py)

### 日本株の一覧を取得し、CSV にする

- getListTickers.py

### ヤフーの株 API にリクエストし、日次で株価の情報を取得する

- getyfinance.py

## Docker で Python 環境構築

### 0. 前提条件

- Linux サーバーまたは仮想環境へのアクセスがあること
- Docker がインストールされていない場合、以下の手順でインストールを行う。

### 1. Docker のインストール

Docker のパッケージをアップデート

```bash
sudo dnf update -y
```

Docker のインストール

```bash
sudo dnf install docker
sudo dnf install curl --allowerasing
# 最新のバージョンを取得
LATEST_VERSION=$(curl -s https://api.github.com/repos/docker/compose/releases/latest | grep -oP '"tag_name": "\K(.*)(?=")')
# ダウンロード
curl -SL "https://github.com/docker/compose/releases/download/${LATEST_VERSION}/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
sudo chmod 750 /usr/local/bin/docker-compose
sudo systemctl start docker
sudo systemctl enable docker
sudo usermod -aG docker $(whoami)
```

ソース

```bash
git clone https://github.com/houmaiwakiri/StockPriceUpDownAI.git
```

### 2. Docker コンテナの構築

Docker イメージのビルド(main.py が実行される)

```bash
cd StockPriceUpDownAI
docker-compose up --build
```

実行終了後、ホスト側のStockPriceUpDownAI/output配下にjapan_stock_data_yyyymmdd.csvが生成される。
