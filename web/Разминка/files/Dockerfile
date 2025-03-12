FROM python:3.10

WORKDIR /app
COPY . .
RUN pip install -r requirements.txt

EXPOSE 5003

CMD ["python", "app.py"]