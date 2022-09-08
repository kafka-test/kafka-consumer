#!/usr/bin/env python

import os
from kafka import KafkaProducer, KafkaConsumer
import json
from bson import json_util

# 'kafka-cluster-kafka-rtlistener-bootstrap-openshift-operators.apps-crc.testing:443'
kafka_server = os.environ['KAFKA_SERVER']
kafka_group = os.environ['KAFKA_GROUP']
kafka_topic = os.environ['KAFKA_TOPIC']

consumer = KafkaConsumer(kafka_topic,
                         group_id=kafka_group,
                         bootstrap_servers = kafka_server,
                         ssl_cafile = '/mnt/kafka-config/ca.crt',
                         security_protocol='SSL',
                         consumer_timeout_ms = 10000,
                         enable_auto_commit=True)

print("Consuming messages from Kafka topic ...")

for message in consumer:
    print ("%s:%d:%d: value=%s" % (message.topic, message.partition, message.offset, message.value))