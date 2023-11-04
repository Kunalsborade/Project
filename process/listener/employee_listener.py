from process.controller.action import create, get, update, delete

import json

def take_action(message):
    try:
        print("In Take Action")
        message_dict = json.loads(message)
        action = message_dict['action']
        data = message_dict['data']
        id = message_dict.get("id")

        if action == "Post":
            create(data)

        if action == "Get":
            get(id)

        if action == "Put":
            update(data,id)

        if action == "Delete":
            delete(id)

    except json.JSONDecodeError as e:
        print(f"Error decoding message: {e}")
    except KeyError as e:
        print(f"Missing key in message: {e}")


