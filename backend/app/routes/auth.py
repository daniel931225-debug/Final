from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from ..schemas import UserCreate
from ..database import get_db
from ..models import User
from ..security import hash_password

router = APIRouter()


@router.post("/register")
async def user_register(
	data: UserCreate, response: Response, db: Session = Depends(get_db)
):
	data_dict = data.model_dump()
	username = data_dict["username"]
	password = data_dict["password"]
	existing_user = db.query(User).where(User.name == username).first()
	if existing_user:
		response.status_code = status.HTTP_400_BAD_REQUEST
		return {"message": "Username already taken"}

	hashed_pwd = hash_password(password)
	db_user = User(name=username, hashed_pwd=hashed_pwd)
	db.add(db_user)
	db.commit()
	db.refresh(db_user)

	return {
		"message": "Successfully registered",
		"data": {"id": db_user.id, "username": db_user.name},
	}
