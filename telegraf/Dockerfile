FROM telegraf:latest

LABEL author="Alexis Le Provost <alexis.leprovost@outlook.com>"
LABEL version="1.0.0"
LABEL description="Telegraf docker image"

USER root

ADD telegraf.template.conf /telegraf.template.conf

RUN apt-get update && apt-get -y install build-essential hddtemp python3

ADD scripts /scripts
ADD run.sh /run.sh

RUN chmod +x /*.sh /scripts/*

RUN apt-get -y install git

ARG PS_DIR=/usr/lib/ps

RUN git clone https://gitlab.com/procps-ng/procps.git ${PS_DIR}

RUN apt-get -y install git gettext autoconf libtool-bin pkg-config gcc make autopoint

WORKDIR ${PS_DIR}

RUN sed -i 's/"\/proc/"\/host\/proc/g' `find . -name "*.c"`
RUN ./autogen.sh
RUN ./configure --without-ncurses
RUN make

RUN rm /bin/ps
RUN ln -s ${PS_DIR}/ps/pscommand /bin/ps

CMD ["/run.sh"]

