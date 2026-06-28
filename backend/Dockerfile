FROM python:3.13-slim

WORKDIR /app

COPY requirements.txt .

# we can also use COPY . . (It means entire folder to be copy from local to container image)

RUN pip install -r requirements.txt --no-cache-dir

COPY main.py .

CMD ["python", "main.py"]

EXPOSE 8000