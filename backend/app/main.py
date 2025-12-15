import uvicorn
from fastapi import FastAPI
from . import models
from .schemas import Config
from .database import engine
from .routes import auth_router, posts_router

models.Base.metadata.create_all(bind=engine)

config = Config()  # type: ignore
app = FastAPI(docs_url=None, redoc_url=None)
app.include_router(auth_router, prefix="/auth")
app.include_router(posts_router, prefix="/posts")

if __name__ == "__main__":
	uvicorn.run(app, host="0.0.0.0", port=config.PORT)
