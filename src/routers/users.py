import logging
from fastapi import APIRouter, status, Depends

from ..utils.send_email import send_activation_email
from ..database.crud.users import create_user, get_all_users
from ..database.database import get_db
from ..schemas import RegisterUser

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/register",status_code=status.HTTP_201_CREATED)
async def create_user_router(body:RegisterUser,db = Depends(get_db)):
    logger.info('/register was called')
    activation_code = create_user(db,body.email,body.password)
    send_activation_email(activation_code)
    return {
        "message": f"User {body.email} created successfully",
        }


# FIXME: This is just a temp endpoint to retrieve the list of users quick
@router.get("/users",status_code=status.HTTP_200_OK)
async def get_users_router(db = Depends(get_db)):
    logger.info('/users was called')    
    response = get_all_users(db)
    if not response:
        return []
    return response
