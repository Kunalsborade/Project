from app import create

import json

def take_action(message):
    try:
        message_dict = json.loads(message)
        action = message_dict['action']
        data = message_dict['data']

        if action == "Post":
            create(data)
        else:
            print(f"Unknown action: {action}")
    except json.JSONDecodeError as e:
        print(f"Error decoding message: {e}")
    except KeyError as e:
        print(f"Missing key in message: {e}")


