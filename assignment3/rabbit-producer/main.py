from pq import RMQProducer
from mess_prod import MessageProducer
import logging
import sys
import os


def make_config(host, port, queue, login, password):
    config = dict()
    config['host'] = host
    config['port'] = port
    config['queue'] = queue
    config['login'] = login
    config['password'] = password
    return config


def main():
    # LOGGING SETTINGS
    logging.basicConfig(stream=sys.stdout, level=logging.INFO)
    ch = logging.StreamHandler(sys.stdout)
    ch.setLevel(logging.DEBUG)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    ch.setFormatter(formatter)
    log = logging.getLogger()
    log.handlers.clear()
    log.addHandler(ch)
    log.info("Start application")

    # RABBIT MQ PRODUCER-CONSUMER SETTINGS
    producer_config = make_config(
        os.environ['RABBIT_IN_HOST'],
        int(os.environ['RABBIT_IN_PORT']),
        os.environ['RABBIT_IN_QUEUE'],
        os.environ['RABBIT_IN_LOGIN'],
        os.environ['RABBIT_IN_PASS']
    )
    # producer_config = make_config("localhost", 5672, "ReadQ", "guest", "guest")
    producer = RMQProducer(producer_config)
    message_producer = MessageProducer(producer)
    message_producer.start_producing()

if __name__ == '__main__':
    main()
