FROM node:12.19.0-alpine
WORKDIR /app
#ENV PATH /app/node_modules/.bin:$PATH
COPY ./package.json ./
COPY ./package-lock.json ./
RUN npm install
#RUN npm install react-scripts@3.4.4 -g --silent
COPY ./public /app/public/
COPY ./src /app/src/

CMD [ "npm","start" ]