import logging
from typing import Annotated

import psycopg
from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

from ..utils.utils import is_expired

from ..database.crud.users import activate_user_by_email, create_user
from ..database.database import get_db
from ..schemas import ActivateUser, RegisterUser
from ..utils.get_current_user import get_current_user
from ..utils.send_email import send_activation_email_factory

logger = logging.getLogger(__name__)

router = APIRouter()

# Basic Auth
security = HTTPBasic()


@router.post("/register", status_code=status.HTTP_201_CREATED)
async def create_user_router(body: RegisterUser, db=Depends(get_db), send_activation_email=Depends(send_activation_email_factory())):
    logger.info("/register was called")
    try:
        activation_code = create_user(db, body.email, body.password)
    except (Exception, psycopg.errors.UniqueViolation) as error:
        logger.error(error)
        raise HTTPException(
            status_code=status.HTTP_409_CONFLICT, detail="Email already in use"
        )
    send_activation_email(body.email, activation_code)
    return {
        "message": f"User {body.email} created successfully",
    }


@router.post("/activate", status_code=status.HTTP_200_OK)
def activate_current_user(
    body: ActivateUser,
    credentials: Annotated[HTTPBasicCredentials, Depends(security)],
    db=Depends(get_db), 
):
    with db as db_connection:
        user = get_current_user(credentials, db_connection)
        if body.activation_code != user.activation_code:
            # Wrong activation code
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The activation_code is not correct",
            )
        if user.is_active:
            return {
                "message": f"User {user.email} is already active. Nothing to do here"
            }
        
        if is_expired(user.activation_code_expiration_time):
            # Wrong activation code
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="The activation_code is not valid anymore. It has reached the expiration limit",
            )

        # The activation code is correct, we update the user to active
        activate_user_by_email(db_connection, user.email)

    return {"message": f"User {user.email} activated."}
