from pydantic import BaseModel


class signUpDetails(BaseModel):
    username: str
    name: str
    password: str
    email: str


class loginDetails(BaseModel):
    password: str
    email: str


class idDetails(BaseModel):
    token: str
