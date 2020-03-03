FROM ubuntu:18.04
RUN apt-get update
RUN apt-get install --yes software-properties-common
RUN add-apt-repository --yes ppa:bitcoin/bitcoin
RUN apt-get update

RUN apt-get install --yes bitcoind make curl net-tools

WORKDIR /src/bitcoin
RUN mkdir -p /root/bitcoind-simnet/

EXPOSE 10340
