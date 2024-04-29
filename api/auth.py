from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session
from db.database import get_session
from ..schemas import User
# models.Base.metadata.create_all(bind=engine)

app = APIRouter(prefix="/auth", tags=["Authentication"])

@app.post("/", response_model=User.User)
def createUser(user: User.UserCreate, db: Session = Depends(get_session)):
    db_user = crud.get_user_by_email(db, email=user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")
    return crud.create_user(db=db, user=user)