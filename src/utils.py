import random

# Generates a random code of 4 digits
def generate_random_code() -> str:
    return '{:04}'.format(random.randint(0, 9999))

def get_password_hash(password:str)->str:
    # TODO: for now we return the same password
    return password