from fastapi import FastAPI
from . import models
from .database import engine
from .routes import auth_router

models.Base.metadata.create_all(bind=engine)

app = FastAPI(docs_url=None, redoc_url=None)
app.include_router(auth_router, prefix="/auth")
