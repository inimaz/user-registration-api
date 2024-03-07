import logging

from fastapi import FastAPI

from .database.database import create_tables, get_db
from .routers import users

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


# Start the application
def start_application():
    logger.info("Starting the application")
    app = FastAPI()
    # Create the db tables
    create_tables(db=get_db())
    add_routing(app)
    return app


def add_routing(app: FastAPI):
    app.include_router(users.router)

    @app.get("/")
    async def root():
        return {"message": "User API root page"}


# Start the application in test mode
def start_test_application():
    logger.info("Starting the test application")
    app = FastAPI()
    # Create the db tables
    add_routing(app)
    return app
