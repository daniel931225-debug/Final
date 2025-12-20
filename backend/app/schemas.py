from typing import Optional
from pydantic import BaseModel, Field


class UserBase(BaseModel):
	username: str


class UserCreate(UserBase):
	password: str = Field(..., min_length=6, max_length=50)


class PostBase(BaseModel):
	title: str
	content: str


class PostCreate(PostBase):
	owner_id: int = Field(..., gt=0)


class PostEdit(BaseModel):
	title: Optional[str] = None
	content: Optional[str] = None
