from kafka import KafkaProducer
import json
topic = 'mytopic'  

# Create a KafkaProducer instance
producer = KafkaProducer(
    bootstrap_servers='localhost:9092' ,
    value_serializer=lambda v: str(v).encode('utf-8')  # Serialize messages as UTF-8 strings
)

# Send a message to the Kafka topic
producer.send(topic, value='@@@@@@@')


producer.close()
