FROM python:3.8.2

# 環境変数を設定
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

# ディレクトリを作成
RUN mkdir /backend-app

# 依存関係をインストール
COPY backend /backend-app

# ワークディレクトリを指定
WORKDIR /backend-app

RUN pip install --upgrade pip

# requirements.txtに記載されたパッケージをインストール
RUN pip install -r /backend-app/requirements.txt

# プロジェクトのファイルをコピー
COPY . /backend-app/

# ポートを開放
CMD python manage.py runserver 0.0.0.0:8000
