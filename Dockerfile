FROM python:3.8.10
WORKDIR /docker-rest-api

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

ENV FLASK_APP=app
ENV FLASK_ENV=development

ENTRYPOINT ["flask", "run",  "--host", "0.0.0.0"]
