from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session 
from ..database import get_db 
from ..import schemas 
from ..import models, schemas
from .. import oauth2

router = APIRouter(
    prefix = "/vote", 
    tags = ['Vote']
)


@router.post("/", status_code=status.HTTP_201_CREATED)
def vote(vote: schemas.Vote, db: Session = Depends(get_db), current_user: int=Depends (oauth2.get_current_user)):
    '''
        A vote direction of 1 means we want to add a vote, a direction of 0 means we want to delete a vote. 
    '''
        
    vote_query = db.query(models.Vote).filter(models.Vote.post_id == vote.post_id, models.Vote.user_id == current_user.id)
    found_vote = vote_query.first() 

    if (vote.dir == 1): 
        #vote already exists 
        if found_vote: 
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,
                                detail=f"user{current_user.id} has already voted on post {vote.post_id}")
        #otherwise add new vote  
        new_vote = models.Vote(post_id = vote.post_id, user_id=current_user.id)
        db.add(new_vote)
        db.commit()
        return {"message": "successfully added vote"}
    
    else:
        if not found_vote: 
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, 
                                detail="Vote does not exist")
        
        #but if we did find a vote, we have to delete it 
        vote_query.delete(synchronize_session=False)
        db.commit()

        return {"message": "successfully deleted vote"}




