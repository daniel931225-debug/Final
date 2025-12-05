from fastapi import HTTPException
from ..security import verify_jwt_token


def auth_dependency(authorization: str | None = None):
	if authorization is None:
		raise HTTPException(status_code=401, detail="Unauthorized")

	jwt_token = authorization.split(" ")[1]
	jwt_payload = verify_jwt_token(jwt_token)
	if jwt_payload is None:
		raise HTTPException(status_code=401, detail="Unauthorized")

	return jwt_payload
