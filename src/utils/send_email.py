import os
import requests
import logging

logger = logging.getLogger(__name__)

def send_activation_email(email:str, activation_code:str):
    EMAIL_SERVER_URL = os.environ.get('EMAIL_SERVER_URL', None)
    data = {"email": f"{email}", "activation_code": f"{activation_code}"}
    logger.info(data)

    # Sending the POST request with the data
    response = requests.post(EMAIL_SERVER_URL, json=data)

    # Checking the response status code
    if response.status_code == 201:
        logger.info(response.json())
    else:
        # If there was an error, print the error message
        logger.error("Error:", response.text)