# Dockerイメージのベースとなるイメージを指定
FROM node:20-alpine

WORKDIR /usr/src/app

COPY /package*.json ./

# コンテナ起動時に実行するコマンドを指定
CMD ["npm", "run", "dev"]
