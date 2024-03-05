import logging
from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.security import HTTPBasic, HTTPBasicCredentials
import psycopg
from typing import Annotated


from ..database.crud.users import activate_user_by_email, create_user, get_all_users
from ..database.database import get_db
from ..schemas import ActivateUser, RegisterUser
from ..utils.get_current_user import get_current_user
from ..utils.send_email import send_activation_email

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/register",status_code=status.HTTP_201_CREATED)
async def create_user_router(body:RegisterUser,db = Depends(get_db), send_email = Depends(send_activation_email)):
    logger.info('/register was called')
    try:
        activation_code = create_user(db,body.email,body.password)
    except (Exception, psycopg.errors.UniqueViolation) as error:
        logger.error(error)
        raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail="Email already in use")
    send_email(body.email, activation_code)
    return {
        "message": f"User {body.email} created successfully",
        }


# FIXME: This is just a temp endpoint to retrieve the list of users quick
@router.get("/users",status_code=status.HTTP_200_OK)
def get_users_router(db = Depends(get_db)):
    logger.info('/users was called')    
    response = get_all_users(db)
    if not response:
        return []
    return response

# Basic Auth
security = HTTPBasic()



@router.get("/users/me")
def read_current_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)], db =Depends(get_db) ):
    with db as db_connection:
        user = get_current_user(credentials,db_connection)
    return {"username": user.email}

@router.post("/activate", status_code=status.HTTP_201_CREATED)
def activate_current_user(
        body:ActivateUser,
        credentials: Annotated[HTTPBasicCredentials, Depends(security)], db =Depends(get_db),
        ):
    with db as db_connection:
        user = get_current_user(credentials,db_connection)
        if body.activation_code != user.activation_code:
            # Wrong activation code
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="The activation_code is not correct")
        if user.is_active:
            return {"message": f"User {user.email} is already active. Nothing to do here" }
        
        # The activation code is correct, we update the user to active
        activate_user_by_email(db_connection, user.email)

    return {"message": f"User {user.email} activated." }