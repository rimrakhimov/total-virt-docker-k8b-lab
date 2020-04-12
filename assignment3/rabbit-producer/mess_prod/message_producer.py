import pika
import logging
import json
import random
import time

log = logging.getLogger(__name__)


class MessageProducer(object):
	def __init__(self, producer):
		log.info("Start initialization")
		self.producer = producer
		self.messageType = {1 : "Type_One", 2 : "Type_Two"}
		self.messageTypeCounter = {1: 0, 2: 0}
		log.info("Finish initialization")

	def start_producing(self):
		log.info("Start producing")
		while (True):
			type = random.randint(1, 2)
			self.producer.publish(json.dumps({
				"type" : self.messageType[type],
				"body" : "This is the message number " + str(self.messageTypeCounter[type]) + " of type " + str(type)
			}))
                        self.messageTypeCounter[type] += 1
			time.sleep(60)



	def stop_producing(self):
		log.info("Finish producing")
