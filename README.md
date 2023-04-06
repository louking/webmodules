# webmodules

This contains various web modules.

The `docker-skeleton-vx.x` version contains skeleton which is suitable to start developing a docker based app.

## development

build: `docker compose build`

run for development: `docker compose -f docker-compose.yml -f docker-compose.dev.yml up -d`

run for production: `docker compose -f docker-compose.yml -f docker-compose.prod.yml up -d`
