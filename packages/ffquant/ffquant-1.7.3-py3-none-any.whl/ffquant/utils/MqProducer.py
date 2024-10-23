from rocketmq.client import Producer, Message
from datetime import datetime
import os
import json

__ALL__ = ['MqProducer']

class MqProducer():
    def __init__(self, *args, **kwargs):
        self.producer = Producer(f"MqProducer_{datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')}")
        server_address = os.environ.get('MQ_SERVER_ADDRESS', '192.168.25.98:9876')
        self.producer.set_name_server_address(server_address)

    def start(self):
        self.producer.start()

    def send(self, name, millis, data):
        msg = Message('index_topic')
        body = {
            "type": name,
            "openTime": millis,
            "closeTime": millis + 60 * 1000,
            "signalKey": "data",
            "signalValue": json.dumps({"data": data})
        }
        msg.set_body(json.dumps(body))
        self.producer.send_sync(msg)    