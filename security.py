from passlib.context import CryptContext
from jose import jwt,JWTError
from fastapi import Depends,HTTPException
from database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import select
from models import User
from datetime import datetime,timezone,timedelta
from fastapi.security import HTTPAuthorizationCredentials,HTTPBearer


SECRET_KEY = "YOUR_SECRET_KEY"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE = 30

pwd_context = CryptContext(schemes=['bcrypt'],deprecated='auto')
security = HTTPBearer()


def hash_password(password):
    return pwd_context.hash(password)


def verify_password(plain_password,hashed_password):
    return pwd_context.verify(plain_password,hashed_password)


def create_access_token(user_id:int):
    expire = datetime.now(timezone.utc) + timedelta(minutes = ACCESS_TOKEN_EXPIRE)


    data = {
        "user_id":user_id,
        "exp":expire
    }

    token = jwt.encode(data,SECRET_KEY,algorithm=ALGORITHM)

    return token


def verify_token(token:str,db:Session):
    try:
        payload = jwt.decode(token,SECRET_KEY,algorithms=[ALGORITHM])

        user_id = payload.get("user_id")
        if not user_id:
            return None

        user = db.execute(select(User).where(User.id == user_id)).scalar_one_or_none()

        if not user:
            return None

        return user
    except JWTError:
        return None


def get_current_user(credentials:HTTPAuthorizationCredentials = Depends(security),db:Session=Depends(get_db)):
    token = credentials.credentials
    user = verify_token(token,db)
    if not user:
        raise HTTPException(
            status_code=401,
            detail = "Invalid token"
        )

    return user