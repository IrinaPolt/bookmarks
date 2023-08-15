FROM python:3.9

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . /app

CMD ["gunicorn", "backend.wsgi:application", "--bind", "0:8000"]