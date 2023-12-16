FROM python:3.10.12-bullseye

WORKDIR /app

RUN apt-get update && apt-get install -y \
    build-essential \
    libssl-dev \
    ca-certificates \
    libasound2 \
    wget \
    ffmpeg \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade pip

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

CMD python main.py
