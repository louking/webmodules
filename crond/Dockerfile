# adapted from https://stackoverflow.com/a/47960145/799921
ARG ALPINE_VER
FROM alpine:${ALPINE_VER}
COPY cronjobs /etc/crontabs/root
RUN apk add --no-cache mysql-client