# Dockerイメージのベースとなるイメージを指定
FROM node:20-alpine

WORKDIR /usr/src/app

COPY /package*.json ./

# 依存関係をインストール
# RUN npm install

# コンテナ起動時に実行するコマンドを指定
CMD ["npm", "start"]
