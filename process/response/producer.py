from kafka import KafkaProducer
import json
import logging

# Configure logging
logger = logging.getLogger('ResponseProducer')
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

def produce_response(message):
    try:
        logger.info("IN produce_response Function")
        response = json.dumps(message)
        topic = 'employee_reply'
        producer = KafkaProducer(
            bootstrap_servers='localhost:9092',
            value_serializer=lambda v: str(v).encode('utf-8')
        )
        producer.send(topic, value=response)
        logger.info("Message sent to gateway: %s", message)
        producer.close()
    except Exception as e:
        logger.error(f"Error producing response: {e}")
