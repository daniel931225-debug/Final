from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from ..schemas import PostCreate, PostEdit
from ..database import get_db
from ..models import User, Post

router = APIRouter()


@router.get("/")
async def get_posts(page: int = 0, db: Session = Depends(get_db)):
	posts = (
		db.query(Post, User.name)
		.join(User, Post.owner_id == User.id)
		.order_by(Post.created_at.desc())
		.limit(10)
		.offset(page * 10)
		.all()
	)

	return {"message": "Successfully fetched posts data", "data": posts}


@router.post("/")
async def create_post(data: PostCreate, db: Session = Depends(get_db)):
	post = Post(**data.model_dump())
	db.add(post)
	db.commit()
	db.refresh(post)
	return {"message": "Post created successfully", "data": post}


@router.put("/{id}")
async def edit_post(id: int, data: PostEdit, db: Session = Depends(get_db)):
	data_dict = data.model_dump(exclude_unset=True)
	if len(data_dict.keys()) == 0:
		return {"message": "No data provided for update"}

	post = db.query(Post).filter(Post.id == id).first()
	if not post:
		return {"message": "Post not found"}

	for key, value in data_dict.items():
		setattr(post, key, value)

	db.commit()
	db.refresh(post)
	return {"message": "Post updated successfully", "data": post}
