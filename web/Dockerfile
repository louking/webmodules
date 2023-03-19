FROM nginx:1.13-alpine
COPY nginx.conf /etc/nginx/nginx.conf
COPY index.html /usr/share/nginx/html/index.html
# https://github.com/phpmyadmin/docker/issues/284#issuecomment-625468269
COPY --from=phpmyadmin/phpmyadmin:5.2.1-fpm /var/www/html /usr/share/nginx/html