FROM python:3.7-alpine

COPY requirements.txt requirements.txt 

RUN pip install --no-cache-dir -r requirements.txt

COPY fetch_joke.py .

CMD [ "python", "-u", "fetch_joke.py"]

ENV JOKE_SERVICE_PORT 5000

EXPOSE ${JOKE_SERVICE_PORT}

