FROM influxdb:1.8

LABEL author="Alexis Le Provost <alexis.leprovost@outlook.com>"
LABEL version="1.0.0"
LABEL description="InfluxDB docker image"

USER root

ADD influxdb.template.conf /influxdb.template.conf

ADD run.sh /run.sh
ENTRYPOINT ["bash", "/run.sh"]
