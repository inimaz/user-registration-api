from fastapi import  FastAPI , status
import logging

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info('Starting the email server mock application')
app = FastAPI()

@app.get("/")
async def root():
    return {"message": "[Email server mock] root page"}



from pydantic import BaseModel, EmailStr

class SendEmailToUser(BaseModel):
    email: EmailStr
    activation_code: str 

@app.post("/",status_code=status.HTTP_201_CREATED)
async def root(data:SendEmailToUser):
    logger.info("Email server has been called")
    logger.info(data)
    return {"message": "[Email server mock] Email sent"}
