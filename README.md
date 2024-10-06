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
sudo systemctl start docker
sudo usermod -aG docker $(whoami)
```

Docker が正常に動作しているか確認

```bash
docker --version
```

Docker を自動起動する設定

```bash
sudo systemctl enable docker
```

### 2. Docker コンテナの構築

Docker イメージのビルド(main.py が実行される)

```bash
cd ~/docker
docker-compose up --build
```

コンテナ接続

```bash
docker exec -it stock-price-updown-ai /bin/bash
```
