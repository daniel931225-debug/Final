from pydantic import BaseModel, Field


class UserBase(BaseModel):
	username: str


class UserCreate(UserBase):
	password: str = Field(..., min_length=6, max_length=50)
