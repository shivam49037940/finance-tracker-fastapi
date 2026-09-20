from fastapi import APIRouter,Depends,HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import select
from database import get_db
from models import Transaction,User
from schemas import TransactionCreate
from security import get_current_user
from datetime import datetime
from calendar import monthrange


router = APIRouter(prefix = '/transactions',tags=["Expenses"])

@router.post("/add")
def create_transaction(
    transaction:TransactionCreate,
    current_user:User = Depends(get_current_user),
    db:Session = Depends(get_db)
):

    new_transaction = Transaction(
        amount = transaction.amount,
        type = transaction.type,
        category = transaction.category,
        description = transaction.description,
        user_id = current_user.id
    )


    db.add(new_transaction)
    db.commit()
    db.refresh(new_transaction)
    return{
        "message":"Transaction added",
        "transaction_id":new_transaction.id
    }