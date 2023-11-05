from process.controller.action import create_employee, get_employee, update_employee, delete_employee, get_all_employee
import json
import logging

# Configure logging
logger = logging.getLogger('MessageProcessor')
logger.setLevel(logging.INFO)
console_handler = logging.StreamHandler()
formatter = logging.Formatter('%(levelname)s - %(message)s')
console_handler.setFormatter(formatter)
logger.addHandler(console_handler)

def process_message(message):
    try:
        logger.info("IN Processing message Function")
        message_dict = json.loads(message)
        action = message_dict['action']
        data = message_dict.get('data')
        id = message_dict.get('id')

        if action == 'Post':
            create_employee(data)
        elif action == 'Get':
            get_employee(id)
        elif action == 'Put':
            update_employee(data, id)
        elif action == 'Delete':
            delete_employee(id)
        elif action == 'Get_all':
            get_all_employee()
        else:
            logger.error(f"Unknown action: {action}")

    except Exception as e:
        logger.error(f"Error processing message: {e}")
