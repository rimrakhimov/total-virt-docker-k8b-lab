FROM python:3.7-alpine

WORKDIR /app

COPY . .
RUN pip install --no-cache-dir -r requirements.txt

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

CMD python main.py
