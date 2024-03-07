import random


# Generates a random code of 4 digits
def generate_random_code() -> str:
    return f"{random.randint(0, 9999):04}"
