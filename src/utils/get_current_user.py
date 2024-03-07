import logging

from fastapi import HTTPException, status

from ..database.crud.users import get_one_user_by_email
from .password_utils import validate_password

logger = logging.getLogger(__name__)


def get_current_user(credentials, db_connection):
    if not credentials or not db_connection:
        raise ValueError("Credentials and db_connection cannot be None")

    current_user_email = credentials.username
    try:
        current_user = get_one_user_by_email(db_connection, current_user_email)
    except Exception as err:
        logger.exception(
            f"Error retrieving user with email '{current_user_email}': {err}"
        )
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    if current_user is None:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )

    is_correct_password = validate_password(
        credentials.password, current_user.password_hash
    )

    if not is_correct_password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Incorrect username or password",
            headers={"WWW-Authenticate": "Basic"},
        )
    return current_user
