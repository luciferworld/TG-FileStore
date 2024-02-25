FROM ubuntu:18.04

ENV DEBIAN_FRONTEND=noninteractive

RUN apt-get update && \
    apt-get install -y locales && \
    locale-gen en_US.UTF-8 && \
    apt-get install -y --no-install-recommends \
        build-essential \
        curl \
        git \
        gnupg2 \
        python3 \
        python3-dev \
        python3-pip \
        python3-lxml \
        pv && \
    apt-get autoclean && \
    apt-get autoremove && \
    rm -rf /var/lib/apt/lists/*

ENV LANG en_US.UTF-8
ENV LC_ALL en_US.UTF-8

RUN pip3 install --upgrade pip setuptools wheel yarl multidict

COPY requirements.txt .

RUN pip3 install -r requirements.txt

COPY . /app

CMD ["python3", "bot.py"]
