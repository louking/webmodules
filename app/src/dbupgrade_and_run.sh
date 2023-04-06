#!/bin/sh
# initial volume create may cause flask db upgrade to fail
while ! flask db upgrade
do
    sleep 5
done
exec "$@"