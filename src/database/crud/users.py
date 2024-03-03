import psycopg
from ...utils.utils import generate_random_code
from ...utils.password_utils import get_password_hash
import logging
logger = logging.getLogger(__name__)

# Function to create a new user in the database
def create_user(db, email, password) -> str:
    activation_code = generate_random_code()
    password_hash = get_password_hash(password)

    try:
        with db as conn:
            # Create a cursor to execute SQL commands
            with conn.cursor() as cursor:
                # Insert user data into the users table
                insert_query = """INSERT INTO users (email, password_hash, activation_code) VALUES (%s, %s, %s)"""
                cursor.execute(insert_query, (email, password_hash, activation_code))
                conn.commit()
        logger.info("User created successfully!")
        return activation_code

    except (Exception, psycopg.DatabaseError) as error:
        logger.error("Error while inserting user into PostgreSQL", error)
        raise error

# Function to get all users of the database
def get_all_users(db, limit = 10):
    try:
        with db as conn:
            # Create a cursor to execute SQL commands
            with conn.cursor() as cursor:
                # Insert user data into the users table
                get_all_query = f"""SELECT * FROM users LIMIT {limit};"""
                cursor.execute(get_all_query)
                # Fetch all rows from the result set
                users = cursor.fetchall()

                logger.info("Get all users retrieved successfully!")
                # Return the fetched users
                return users

    except (Exception, psycopg.DatabaseError) as error:
        logger.error("Error while retrieving all users from PostgreSQL", error)
        raise error
# Function to get one user from the database
def get_one_user(db, user_id):
    try:
        with db as conn:
            # Create a cursor to execute SQL commands
            with conn.cursor() as cursor:
                # Insert user data into the users table
                get_all_query = f"""SELECT * FROM users WHERE id = {user_id};"""
                cursor.execute(get_all_query)
                # Fetch all rows from the result set
                users = cursor.fetchall()
                logger.info(f"Get user {user_id} replied successfully!")
                # Return the fetched users
                assert len(users) == 1
                return users[0]

    except (Exception, psycopg.DatabaseError) as error:
        logger.error("Error while retrieving one user from PostgreSQL", error)
        raise error


# Function to patch one user from the database
def patch_user(db, user_id ):
    # TODO
    pass