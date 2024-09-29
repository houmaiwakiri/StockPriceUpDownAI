# 株価予測

## 処理(main.py)

### 日本株の一覧を取得し、CSVにする

- getListTickers.py

### ヤフーの株APIにリクエストし、日次で株価の情報を取得する

- getyfinance.py

## DockerでPython環境構築

### 0. 前提条件

- Linuxサーバーまたは仮想環境へのアクセスがあること
- Dockerがインストールされていない場合、以下の手順でインストールを行う。

### 1. Docker のインストール

  Dockerのパッケージをアップデート

  ```bash
  sudo dnf update -y
  ```

  Dockerのインストール

  ```bash
  sudo dnf install docker
  sudo systemctl start docker
  sudo usermod -aG docker $(whoami)
  ```

  Dockerが正常に動作しているか確認

  ```bash
  docker --version
  ```

  Dockerを自動起動する設定

  ```bash
  sudo systemctl enable docker
  ```

### 2. Dockerコンテナの構築

  Dockerfile の作成

  ```bash
  mkdir -p ~/docker/stock-price-updown-ai/
  vim ~/docker/stock-price-updown-ai/dockerfile
  ```

  記述内容

  ```shell
  FROM python:3.8-slim

  WORKDIR /app

  RUN pip install --upgrade pip
  RUN pip install requests beautifulsoup4 pandas yfinance

  RUN apt-get update && apt-get install -y git
  RUN git clone https://github.com/houmaiwakiri/StockPriceUpDownAI.git

  WORKDIR /app/stock-price-updown-ai

  ENV PYTHONUNBUFFERED=1
  ```

  Dockerイメージのビルド Dockerfileがあるディレクトリに移動して以下を実行します。

  ```bash
  cd ~/docker/stock-price-updown-ai/
  docker build -t stock-price-updown-ai .
  ```

コンテナの実行 コンテナを実行してプログラムを動かします。

  ```bash
  docker run -it stock-price-updown-ai
  ```
