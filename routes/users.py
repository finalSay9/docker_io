from fastapi import APIRouter, HTTPException, status, Depends
from schemas import CreateUser, UserResponse
from sqlalchemy.orm import Session
from dependency import get_db
from models import User
from security import hash_password


router = APIRouter(
    prefix='/users',
    tags=['users']
)


@router.post('/create', status_code=status.HTTP_201_CREATED, response_model=UserResponse)
def create_user(user: CreateUser, db: Session=Depends(get_db)):
    #check if email already exist
    exsting_email=db.query(User).filter(User.email == user.email).first()
    if exsting_email:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Email already exist")
    
    new_user = User(
        username=user.username,
        email=user.email,
        fullname=user.fullname,
        gender=user.gender,
        hashed_password=hash_password(user.password)
    )
    db.add(new_user)
    db.commit()
    db.refresh(new_user)

    return new_user