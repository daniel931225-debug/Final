import bcrypt
import os
from jose import jwt


def hash_password(password: str):
	return bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")


def verify_jwt_token(token: str):
	try:
		payload = jwt.decode(token, os.getenv("JWT_SECRET"), algorithms=["HS256"])
		return payload
	except:
		return None
