FROM python:3.11
WORKDIR /app

COPY . .
COPY requirements.txt .


RUN pip install --upgrade pip && \
    pip install -r /app/requirements.txt && \
    pip install .

CMD ["python3", "src/main.py"]
