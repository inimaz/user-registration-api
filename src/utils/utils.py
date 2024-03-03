import random
# Generates a random code of 4 digits
def generate_random_code() -> str:
    return '{:04}'.format(random.randint(0, 9999))