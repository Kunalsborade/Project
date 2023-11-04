from kafka import KafkaConsumer
import logging
from process.listener.employee_listener import process_message

logger = logging.getLogger('KafkaConsumer')
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

# Configuration
kafka_server = 'localhost:9092'
topic = 'employee'

# Create a Kafka consumer instance
consumer = KafkaConsumer(
    topic,
    bootstrap_servers=kafka_server,
    auto_offset_reset='latest',
    enable_auto_commit=True,
    auto_commit_interval_ms=1000,
    value_deserializer=lambda x: x.decode('utf-8')
)

# Subscribe to the specified topic
consumer.subscribe(topics=[topic])
logger.info("Kafka Consumer Started")

# Process incoming messages
for message in consumer:
    logger.info(f"Received message: {message.value}")
    message_value = message.value

    try:
        process_message(message_value)
    except Exception as e:
        logger.error(f"Error processing message: {e}")
