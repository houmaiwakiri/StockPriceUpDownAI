# 株価予測 + Sphinx

## 処理(main.py)

### 日本株の一覧を取得し、CSVにする

getListTickers.py

### ヤフーの株APIにリクエストし、日次で株価の情報を取得する

getyfinance.py

## DockerでPython環境構築 + Sphinx導入

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
  sudo amazon-linux-extras install docker
  sudo service docker start
  sudo usermod -a -G docker $(whoami)
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
  vim ~/docker/StockPriceUpDownAI/dockerfile
  ```

  記述内容

  ```shell
  FROM python:3.8-slim

  WORKDIR /app

  RUN pip install --upgrade pip
  RUN pip install yfinance sphinx sphinx-rtd-theme

  RUN apt-get update && apt-get install -y git
  RUN git clone https://github.com/houmaiwakiri/StockPriceUpDownAI.git

  WORKDIR /app/StockPriceUpDownAI

  ENV PYTHONUNBUFFERED=1
  ```

  Dockerイメージのビルド Dockerfileがあるディレクトリに移動して以下を実行します。

  ```bash
  cd ~/docker/StockPriceUpDownAI/
  docker build -t StockPriceUpDownAI .
  ```

コンテナの実行 コンテナを実行してプログラムを動かします。

  ```bash
  docker run -it StockPriceUpDownAI
  ```

### 3. Sphinx ドキュメンテーションの生成

コンテナ内でSphinxの初期設定
プロンプトに従ってプロジェクト名や著者名を入力

  ```bash
  sphinx-quickstart
  ```

設定ファイルの編集 conf.py で必要な設定を行います。例えば、テーマを指定する場合は以下のようにします

設定ファイルの編集

  ```bash
  vim conf.py
  ```

ドキュメント(.rst) ファイルを作成

  ```bash
  make html
  ```
