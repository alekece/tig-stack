#!/bin/bash

set -m
CONFIG_TEMPLATE="/telegraf.template.conf"
CONFIG_FILE="/etc/telegraf/telegraf.conf"

sed -e "s/\${HOST_NAME}/$HOST_NAME/" \
    -e "s!\${INFLUXDB_HOST}!$INFLUXDB_HOST!" \
    -e "s/\${INFLUXDB_PORT}/$INFLUXDB_PORT/" \
    -e "s/\${DATABASE}/$DATABASE/" \
    $CONFIG_TEMPLATE > $CONFIG_FILE

echo "=> Starting Telegraf ..."

exec telegraf -config /etc/telegraf/telegraf.conf
