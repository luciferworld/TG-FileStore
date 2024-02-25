# Use the official Ubuntu 18.04 image as the base
FROM ubuntu:18.04

# Set environment variables to prevent interactive prompts during package installations
ENV DEBIAN_FRONTEND=noninteractive \
    LANG=en_US.UTF-8 \
    LC_ALL=en_US.UTF-8

# Update package lists and install necessary packages
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        locales \
        build-essential \
        curl \
        git \
        gnupg2 \
        python3 \
        python3-dev \
        python3-pip \
        python3-lxml \
        pv && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Upgrade pip and install necessary Python packages
RUN pip3 install --upgrade pip setuptools wheel yarl multidict

# Copy the requirements file and install Python dependencies
COPY requirements.txt /app/
RUN pip3 install -r /app/requirements.txt
RUN pip3 install --upgrade pyrogram

# Copy the bot.py file into the /app directory
COPY bot.py /app/

# Set the working directory to /app
WORKDIR /app

# Specify the command to run when the container starts
CMD ["python3", "bot.py"]
