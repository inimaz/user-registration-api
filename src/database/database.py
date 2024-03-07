import logging
import os
from contextlib import contextmanager

import psycopg

logger = logging.getLogger(__name__)
POSTGRESQL_DATABASE_URL = os.environ.get("DATABASE_URL", None)
TABLES = [
    """
        CREATE TABLE IF NOT EXISTS users (
            id SERIAL PRIMARY KEY,
            email VARCHAR(255) UNIQUE NOT NULL,
            password_hash VARCHAR(255) NOT NULL,
            activation_code CHAR(4) NOT NULL,
            is_active BOOLEAN NOT NULL DEFAULT FALSE
        );
    """
]


@contextmanager
def get_db():
    if not POSTGRESQL_DATABASE_URL:
        raise ValueError("DATABASE_URL must be defined")
    logger.info("Starting a db connection")
    conn = psycopg.connect(POSTGRESQL_DATABASE_URL)
    try:
        yield conn
    finally:
        if conn is not None:
            conn.close()
            logger.info("Connection closed")


def create_tables(db):
    with db as conn:
        with conn.cursor() as cur:
            for table_query in TABLES:
                cur.execute(table_query)
        conn.commit()


def drop_tables(db):
    with db as conn:
        with conn.cursor() as cur:
            cur.execute(f"DROP TABLE IF EXISTS users;")
        conn.commit()
