FROM python:3.7-alpine

WORKDIR /app

#RUN apk add --virtual .build-deps gcc python3-dev musl-dev postgresql-dev

COPY . .
#RUN pip install --no-cache-dir -r requirements.txt
RUN apk update && apk add --no-cache --virtual .build-deps\
    postgresql-dev gcc libpq  python3-dev musl-dev linux-headers\
    && pip install --no-cache-dir -r requirements.txt\
    && apk del .build-deps\
    && rm -rf /var/cache/apk/*

# configs of the queue consumer will read messages from
ENV RABBIT_IN_HOST=127.0.0.1
ENV RABBIT_IN_PORT=5672
ENV RABBIT_IN_LOGIN=guest
ENV RABBIT_IN_PASS=guest
ENV RABBIT_IN_QUEUE=ReadQ

# configs of the queue consumer will write status messages to
ENV RABBIT_OUT_HOST=127.0.0.1
ENV RABBIT_OUT_PORT=5672
ENV RABBIT_OUT_LOGIN=guest
ENV RABBIT_OUT_PASS=guest
ENV RABBIT_OUT_QUEUE=WriteQ

# postgreSql configuration
ENV DB_HOST=127.0.0.1
ENV DB_PORT=5432
ENV DB_NAME=rabbit
ENV DB_USERNAME=admin
ENV DB_PASS=admin

CMD python main.py
