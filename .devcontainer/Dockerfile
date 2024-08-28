FROM "mcr.microsoft.com/devcontainers/base:bullseye"

RUN apt-get update && apt-get install -y build-essential \
    libbz2-dev \
    libncurses5-dev \
    libffi-dev \
    libreadline-dev \
    libsqlite3-dev \
    tk-dev \
    liblzma-dev \
    libssl-dev \
    curl

    # Install Python3 and pip
RUN apt update && apt install python3 python3-pip -y