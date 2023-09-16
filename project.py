from kafka import KafkaConsumer
from logging import Logger
from process.listener.employee_listener import take_action
import json

topic = 'employee'

consumer = KafkaConsumer(
    topic,
    bootstrap_servers='localhost:9092',  
    auto_offset_reset='latest',  
    enable_auto_commit=True,  
    auto_commit_interval_ms=1000,  
    value_deserializer=lambda x: x.decode('utf-8') 
)
consumer.subscribe(topics=topic)

for message in consumer:
    print(f"Received message: {message.value}")
 
    res = message.value
    ress = json.loads(res)
    try:
        take_action(message.value)
    except Exception as e:
        print(e)
