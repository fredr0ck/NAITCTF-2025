FROM python:3.10

RUN apt-get update && apt-get install -y \
    wget \
    curl \
    gnupg \
    libnss3 \
    libgdk-pixbuf2.0-0 \
    libdbus-1-3 \
    libasound2 \
    libatk-bridge2.0-0 \
    libatk1.0-0 \
    libcups2 \
    libx11-xcb1 \
    libxcomposite1 \
    libxrandr2 \
    libgdk-pixbuf2.0-0 \
    libnspr4 \
    libxtst6 \
    xdg-utils \
    chromium


WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

EXPOSE 5001

CMD ["python", "app.py"]
