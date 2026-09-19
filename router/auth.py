from fastapi import APIRouter,Depends
from sqlalchemy.orm import Session
from database import get_db
from schemas import UserCreate,UserLogin

router = APIRouter(prefix = "/auth",tags=['Authentication'])


@router.post('/register')
def register(user:UserCreate,db:Session=Depends(get_db)):
    pass