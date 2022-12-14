#!/usr/bin/env python

import os
from kafka import KafkaConsumer
from json import loads

# 'kafka-cluster-kafka-rtlistener-bootstrap-openshift-operators.apps-crc.testing:443'
kafka_server = os.environ['KAFKA_SERVER']
kafka_group = os.environ['KAFKA_GROUP']
kafka_topic = os.environ['KAFKA_TOPIC']

#  ssl_cafile = '/mnt/kafka-config/ca.crt',
consumer = KafkaConsumer(kafka_topic,
                         group_id=kafka_group,
                         bootstrap_servers = kafka_server,
                         ssl_cafile = '/vault/secrets/ca.crt',
                         security_protocol='SSL',
                         consumer_timeout_ms = 10000,
                         enable_auto_commit=True,
                         auto_offset_reset='earliest',
                         value_deserializer=lambda x: loads(x.decode('utf-8')))

print("Consuming messages from Kafka topic ...")

try:
    for message in consumer:
        try:
            print ("[topic: {}]:[partition: {}]:[offset: {}] {}".format(message.topic, message.partition, message.offset, message.value))
        except:
            print("Unable to read the message")
except Exception as e:
    print(e)