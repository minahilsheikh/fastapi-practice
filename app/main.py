from fastapi import FastAPI, status, Response, HTTPException, Depends
from typing import List
from fastapi import Body
from pydantic import BaseModel
from random import randrange
import psycopg2
import time
from psycopg2.extras import RealDictCursor
from . import models, schemas, utils
from . database import engine, get_db
from sqlalchemy.orm import Session
from . routers import post, user, auth


models.Base.metadata.create_all(bind=engine)

app = FastAPI() 


while True: 

    try: 
        conn = psycopg2.connect(host='localhost', database='socialmediaapi', user='postgres', password='foobar', cursor_factory=RealDictCursor)
        cursor = conn.cursor() 
        print("Database connection was successfull!")
        break 
    except Exception as error: 
        print("Connecting to database failed")
        print("Error: ", error)

app.include_router(post.router)
app.include_router(user.router)
app.include_router(auth.router)