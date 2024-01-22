FROM klakegg/hugo:alpine as HUGO
RUN apk add --update npm
WORKDIR /static-site
COPY package.json .
RUN npm install
COPY . ./
RUN hugo -v --source=/static-site --destination=/static-site/public

FROM nginx
COPY --from=HUGO /static-site/public/. /usr/share/nginx/html/
EXPOSE 80
