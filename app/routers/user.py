from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session
from typing import List 
from .. import models, schemas, utils
from .. database import engine, get_db

router = APIRouter(
    prefix = "/users", 
    tags = ['Users']
)

@router.get("/")
def get_users(db:Session=Depends(get_db)):

    users = db.query(models.User).all() 
    return users 

@router.get('/{id}', response_model=schemas.UserOut)
def get_user(id:int, db:Session = Depends(get_db)): 
    user = db.query(models.User).filter(models.User.id == id).first()
    
    if not user: 
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                            detail=f"User with id: {id} does not exist")
    
    return user 

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.UserOut)
def create_users(user: schemas.UserCreate, db: Session = Depends(get_db)): 
        
    #hash the password - user.password 
    hashed_password = utils.hash(user.password)
    user.password = hashed_password

    new_user = models.User(**user.model_dump())
    db.add(new_user) 
    db.commit()   
    db.refresh(new_user)

    return new_user