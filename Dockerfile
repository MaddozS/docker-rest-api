FROM python:3.8.10
WORKDIR /docker-rest-api

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT [ "python", "app.py" ]
