FROM python:alpine
MAINTAINER Charlie Gildawie <charlie@skyscanner.net>

COPY *.py ./
COPY requirements.txt .
EXPOSE 8080

RUN apk add --update py-pip gcc g++ linux-headers\
 && pip install -r requirements.txt \
 && apk del py-pip gcc g++ linux-headers

ENTRYPOINT ["python", "dojo.py"]
