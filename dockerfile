FROM python:3.12.1-slim

RUN apt-get update && apt-get install -y \
    python3-tk \
    tk8.6-dev \
    libx11-6 \
    libglib2.0-0 \
    curl && \
    rm -rf /var/lib/apt/lists/* && \
    curl -sSL https://github.com/jwilder/dockerize/releases/latest/download/dockerize-linux-amd64-v0.8.1.tar.gz | tar -xz -C /usr/local/bin
WORKDIR /app
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8000  
CMD ["dockerize", "-wait", "tcp://db:3306", "-timeout", "30s", "python", "app.py"]
