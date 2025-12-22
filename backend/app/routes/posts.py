from typing import Any
from fastapi import APIRouter, Depends, Response, status
from sqlalchemy.orm import Session
from sqlalchemy.exc import SQLAlchemyError, IntegrityError
from ..schemas import PostCreate, PostEdit
from ..database import get_db
from ..models import User, Post
from ..dependencies import auth_dependency

router = APIRouter()


@router.get("/")
async def get_posts(response: Response, page: int = 0, db: Session = Depends(get_db)):
	try:
		posts = (
			db.query(Post, User.name)
			.join(User, Post.owner_id == User.id)
			.order_by(Post.created_at.desc())
			.limit(10)
			.offset(page * 10)
			.all()
		)

		return {"message": "Successfully fetched posts data", "data": posts}
	except SQLAlchemyError as e:
		print(e)
		response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
		return {"message": "An error occurred while fetching posts data"}


@router.post("/")
async def create_post(
	data: PostCreate,
	response: Response,
	_: dict[str, Any] = Depends(auth_dependency),
	db: Session = Depends(get_db),
):
	try:
		post = Post(**data.model_dump())
		db.add(post)
		db.commit()
		db.refresh(post)
		response.status_code = status.HTTP_201_CREATED
		return {"message": "Post created successfully", "data": post}
	except IntegrityError as e:
		print(e)
		db.rollback()
		response.status_code = status.HTTP_400_BAD_REQUEST
		return {"message": "Invalid data provided"}
	except SQLAlchemyError as e:
		print(e)
		db.rollback()
		response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
		return {"message": "An error occurred while creating the post"}


@router.put("/{id}")
async def edit_post(
	id: int,
	data: PostEdit,
	response: Response,
	jwt_payload: dict[str, Any] = Depends(auth_dependency),
	db: Session = Depends(get_db),
):
	data_dict = data.model_dump(exclude_unset=True)
	if len(data_dict.keys()) == 0:
		return {"message": "No data provided for update"}

	post = db.query(Post).filter(Post.id == id).first()
	if not post:
		response.status_code = status.HTTP_404_NOT_FOUND
		return {"message": "Post not found"}
	if post.owner_id != jwt_payload["user_id"]:
		response.status_code = status.HTTP_403_FORBIDDEN
		return {"message": "You are not authorized to edit this post"}

	for key, value in data_dict.items():
		setattr(post, key, value)

	db.commit()
	db.refresh(post)
	return {"message": "Post updated successfully", "data": post}


@router.delete("/{id}")
async def delete_post(
	id: int,
	response: Response,
	jwt_payload: dict[str, Any] = Depends(auth_dependency),
	db: Session = Depends(get_db),
):
	post = db.query(Post).filter(Post.id == id).first()
	if not post:
		response.status_code = status.HTTP_404_NOT_FOUND
		return {"message": "Post not found"}
	if post.owner_id != jwt_payload["user_id"]:
		response.status_code = status.HTTP_403_FORBIDDEN
		return {"message": "You are not authorized to delete this post"}

	db.delete(post)
	db.commit()
	return {"message": "Post deleted successfully"}
