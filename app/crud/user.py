from app.models.user import User
from sqlalchemy.orm import Session

def get_or_create_user(db: Session, email: str):
    user = db.query(User).filter(User.email == email).first()
    if not user:
        user = User(email=email, role="customer") 
        db.add(user)
        db.commit()
        db.refresh(user)
    return user
