from kafka import KafkaProducer
import json

def get_payload(id):
    """
    Create a payload dictionary with action and data.

    Args:
        action (str): The action to be included in the payload.
        data (dict): The data to be included in the payload.

    Returns:
        dict: The payload dictionary.
    """
    payload = {
        "message": "Successfuly Created",
        "id": id
    }
    message = json.dumps(payload)
    return message

def produce_responce(message):
    ans = get_payload(message)
    print(ans)
    
    topic = 'employee_reply'  
    producer = KafkaProducer(
        bootstrap_servers='localhost:9092' ,
        value_serializer=lambda v: str(v).encode('utf-8')  
    )
    producer.send(topic, value = ans)
    producer.close()