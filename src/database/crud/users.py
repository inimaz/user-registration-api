import logging

import psycopg

from ...utils.password_utils import get_password_hash
from ...utils.utils import generate_random_code

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
def get_all_users(db, limit=10):
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
def get_one_user_by_email(connection, email):
    try:
        with connection.cursor() as cursor:
            # Insert user data into the users table
            get_one_query = f"""SELECT * FROM users WHERE email = '{email}';"""
            cursor.execute(get_one_query)
            # Fetch all rows from the result set
            users = cursor.fetchall()
            logger.info(f"Get user {email} replied successfully!")
            # Return the fetched users
            assert len(users) == 1
            user = users[0]
            return User(user)

    except (Exception, psycopg.DatabaseError) as error:
        logger.error("Error while retrieving one user from PostgreSQL", error)
        raise error


# Function to activate one user, having the email as input
def activate_user_by_email(connection, email):
    try:
        with connection.cursor() as cursor:
            # Insert user data into the users table
            update_is_active_query = f"""
                UPDATE users
                SET is_active = true
                WHERE email = '{email}';
            """
            cursor.execute(update_is_active_query)
            connection.commit()
            logger.info(f"User {email} updated successfully!")

    except (Exception, psycopg.DatabaseError) as error:
        logger.error(f"Error while updating user {email} in PostgreSQL")
        logger.error(str(error))
        raise error


# Wrap class to return a meaningful object in the CRUD
class User:
    def __init__(self, user_tuple):
        self.id = user_tuple[0]
        self.email = user_tuple[1]
        self.password_hash = user_tuple[2]
        self.activation_code = user_tuple[3]
        self.is_active = user_tuple[4]

    def __str__(self):
        return f"User(id={self.id}, user_email={self.email}, password_hash={self.password_hash}, activation_code={self.activation_code}, is_active={self.is_active})"
