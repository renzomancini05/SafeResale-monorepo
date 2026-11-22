FROM node:22-alpine

WORKDIR /app

#evita di reinstallare i pacchetti a ogni rebuild
COPY package*.json ./
RUN npm ci

COPY . .
RUN npm run build

EXPOSE 3000

CMD ["npm", "start"]