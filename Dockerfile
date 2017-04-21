FROM python:3-alpine
MAINTAINER Charlie Gildawie <charlie@skyscanner.net>

COPY *.py ./
COPY requirements.txt .

RUN apk add --update py-pip gcc g++ linux-headers\
 && pip3 install -r requirements.txt \
 && apk del py-pip gcc g++ linux-headers

ENTRYPOINT ["python", "dojo.py", "--cpu_target=80"]
