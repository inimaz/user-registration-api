import logging
from fastapi import APIRouter, status, Depends

from ..schemas import RegisterUser

logger = logging.getLogger(__name__)

router = APIRouter()

@router.post("/register",status_code=status.HTTP_201_CREATED)
async def create_user(body:RegisterUser):
    logger.info('/register was called')    
    return body