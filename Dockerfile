FROM python:3.7-alpine

COPY requirements.txt requirements.txt 

RUN pip install --no-cache-dir -r requirements.txt

COPY service/fetch_joke.py .

CMD [ "python", "-u", "fetch_joke.py"]

ENV JOKE_SERVICE_PORT 5000

ENV JOKE_URI 'http://api.icndb.com/jokes/random?firstName={first_name}&lastName={last_name}&limitTo=[nerdy];'

ENV NAME_URI 'https://api.namefake.com/'

ENV JOKE_SERVICE_PORT 5000

EXPOSE ${JOKE_SERVICE_PORT}
