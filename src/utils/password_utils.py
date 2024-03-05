import bcrypt

# Generates a password hash to store in the db
def get_password_hash(password:str)->str:
    # Generate a salt and hash the password
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(password.encode('utf-8'), salt)
    # Return the hashed password as a string
    return hashed_password.decode('utf-8')

# Validates that the stored hash password is the same as the one for password
def validate_password (password: str, hashed_password:str) -> bool:
    if not hashed_password:
        return False
    # Check if the provided password matches the hashed password
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))