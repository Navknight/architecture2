FROM ubuntu:20.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        software-properties-common \
        build-essential \
        make \
        ca-certificates && \
    add-apt-repository -y ppa:ubuntu-toolchain-r/test && \
    apt-get update && \
    apt-get install -y gcc-7 g++-7 && \
    update-alternatives --install /usr/bin/g++ g++ /usr/bin/g++-7 0 && \
    update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-7 0 && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /workspace
