# 公式からpython3.8 on alpine linuxイメージをpull
FROM python:3.8-alpine

# 作業ディレクトリを設定
WORKDIR /new-pointplus

# 環境変数を設定
# Pythonがpyc filesとdiscへ書き込むことを防ぐ
ENV PYTHONDONTWRITEBYTECODE 1
# Pythonが標準入出力をバッファリングすることを防ぐ
ENV PYTHONUNBUFFERED 1

# Pipenvをインストール
RUN pip install --upgrade pip \
&& pip install pipenv

# ホストのpipfileをコンテナの作業ディレクトリにコピー
COPY ./Pipfile /new-pointplus/Pipfile

# pipfileからパッケージをインストールしてDjango環境を構築
RUN pipenv install --skip-lock --system --dev

# MySQL接続ドライバー
#RUN pip install mysql-connector-python
#RUN pip install PyMySQL
#RUN apk add --no-cache build-base mariadb-connector-c-dev
#RUN pip install mysqlclient>=1.4.4

RUN apk update && apk add --no-cache \
    gcc \
    build-base \
    mariadb-connector-c-dev \
    linux-headers \
    mariadb-connector-c-dev \
    libffi-dev \
    mysql-dev \
    python3-dev && \
    pip3 install --upgrade pip

RUN pip install mysqlclient>=1.4.4

# ホストのカレントディレクトリ（現在はappディレクトリ）を作業ディレクトリにコピー
COPY . /new-pointplus/