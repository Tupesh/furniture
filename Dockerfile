FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
#no-cache-dir helps to reduce image size by not caching the installed packages

COPY . .

EXPOSE 8000


ENTRYPOINT [ "python" ]

CMD ["manage.py", "runserver", "0.0.0.0:8000"]
