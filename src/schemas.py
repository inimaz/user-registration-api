from pydantic import BaseModel, EmailStr


class RegisterUser(BaseModel):
    email: EmailStr
    password: str


class ActivateUser(BaseModel):
    activation_code: str
