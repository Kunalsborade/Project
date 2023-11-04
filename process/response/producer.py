from kafka import KafkaProducer
import json

def produce_responce(message):   
    response = json.dumps(message)
    topic = 'employee_reply'  
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092' ,
        value_serializer=lambda v: str(v).encode('utf-8')  
    )
    producer.send(topic, value = response)
    print("Message sent to gateway :", message)
    producer.close()