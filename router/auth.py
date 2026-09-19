from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas import UserCreate,UserLogin
from models import User
from security import hash_password

router = APIRouter(prefix = "/auth",tags=['Authentication'])


@router.post('/register')
def register(user:UserCreate,db:Session=Depends(get_db)):
    password = hash_password(user.password)

    new_user = User(
        name = user.name,
        email = user.email,
        hash_password = password
    )

    db.add(new_user)
    db.commit()
    db.refresh(new_user)


    return{
        "message":"ser registered successfully",
        "user_id":new_user.id
    }

    