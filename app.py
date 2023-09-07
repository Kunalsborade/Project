# from flask import Flask
# from flask_sqlalchemy import SQLAlchemy

# app = Flask(__name__) 

# app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://kunal/kb@526688@localhost:5432/project'
# db = SQLAlchemy(app)
# app.

from kafka import KafkaConsumer

topic = 'employee'

# Create a KafkaConsumer instance
consumer = KafkaConsumer(
    topic,
    bootstrap_servers='localhost:9092',  # Replace with your Kafka server address
    auto_offset_reset='latest',  # Start consuming from the latest offset
    enable_auto_commit=True,  # Automatically commit offsets
    auto_commit_interval_ms=1000,  # Commit offsets every 1 second (adjust as needed)
    value_deserializer=lambda x: x.decode('utf-8')  # Deserialize message values as strings
)

# Start consuming messages
for message in consumer:
    print(f"Received message: {message.value}")


