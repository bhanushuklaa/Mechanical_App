from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import random
import string

from app.schemas.user import UserLogin, OTPRequest, OTPVerify, TokenResponse
from app.database import SessionLocal
from app.services.auth_service import authenticate_user
from app.core.security import create_access_token
from app.core.config import settings
from app.models.otp import EmailOTP
from app.models.user import User
from app.utils.email_sender import send_email_otp
from app.crud.user import get_or_create_user

router = APIRouter(prefix="/api/v1/auth", tags=["Auth"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# ---------------------------
# 1. LOGIN WITH PASSWORD
# ---------------------------

@router.post("/login")
def login(user_data: UserLogin, db: Session = Depends(get_db)):
    user = authenticate_user(db, user_data.email, user_data.password)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Invalid credentials")

    access_token = create_access_token(
        data={"sub": user.email, "user_id": user.id, "role": user.role},
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    return {"access_token": access_token, "token_type": "bearer"}

# ---------------------------
# 2. SEND OTP TO EMAIL
# ---------------------------

otp_requests = {}

@router.post("/request-otp")
def request_otp(data: OTPRequest, db: Session = Depends(get_db)):
    email = data.email
    now = datetime.utcnow()

    # Rate limit: max 3 OTP requests per minute
    requests = otp_requests.get(email, [])
    requests = [t for t in requests if (now - t).seconds < 60]
    if len(requests) >= 3:
        raise HTTPException(status_code=429, detail="Too many OTP requests. Try again later.")

    otp = ''.join(random.choices(string.digits, k=6))
    expires_at = now + timedelta(minutes=5)

    db_otp = EmailOTP(email=email, otp=otp, expires_at=expires_at)
    db.add(db_otp)
    db.commit()

    send_email_otp(email=email, otp=otp)

    requests.append(now)
    otp_requests[email] = requests

    return {"msg": "OTP sent to your email"}

# ---------------------------
# 3. VERIFY OTP + RETURN JWT
# ---------------------------
@router.post("/verify-otp", response_model=TokenResponse)
def verify_otp(data: OTPVerify, db: Session = Depends(get_db)):
    otp_record = db.query(EmailOTP).filter(
        EmailOTP.email == data.email,
        EmailOTP.otp == data.otp,
        EmailOTP.expires_at > datetime.utcnow()
    ).first()

    if not otp_record:
        raise HTTPException(status_code=400, detail="Invalid or expired OTP")

    db.delete(otp_record)
    db.commit()

    user = get_or_create_user(db, data.email)

    access_token = create_access_token(
        data={"sub": user.email, "user_id": user.id, "role": user.role},
        expires_delta=timedelta(minutes=settings.ACCESS_TOKEN_EXPIRE_MINUTES)
    )

    return TokenResponse(access_token=access_token, token_type="bearer")
