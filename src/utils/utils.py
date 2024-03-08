import random
from datetime import datetime, timedelta

# Generates a random code of 4 digits and its expiration time
def generate_random_code_and_expiration_time() -> tuple:
    activation_code = f"{random.randint(0, 9999):04}"
    current_time = datetime.now()
    expiration_time = current_time + timedelta(minutes=1)  # Set expiration time to one minute from now
    return activation_code, expiration_time

# True if current date is higher than the given expiration time
def is_expired (expiration_time):
    return datetime.now() > expiration_time