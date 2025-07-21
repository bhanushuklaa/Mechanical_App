from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from datetime import datetime, timedelta
import random
from app.schemas.email_otp import EmailSchema, OTPVerifySchema
from app.utils.email_sender import send_email_otp
from app.models.email_otp import EmailOTP
from app.dependencies import get_db

router = APIRouter()

@router.post("/auth/request-otp")
def request_otp(payload: EmailSchema, db: Session = Depends(get_db)):
    otp = str(random.randint(100000, 999999))

    success = send_email_otp(payload.email, otp)
    if not success:
        raise HTTPException(status_code=500, detail="Failed to send OTP email.")

    expires = datetime.utcnow() + timedelta(minutes=5)

    db.query(EmailOTP).filter(EmailOTP.email == payload.email).delete()
    db.add(EmailOTP(email=payload.email, otp=otp, expires_at=expires))
    db.commit()
    return {"msg": "OTP sent to email."}


@router.post("/auth/verify-otp")
def verify_otp(payload: OTPVerifySchema, db: Session = Depends(get_db)):
    record = db.query(EmailOTP).filter(EmailOTP.email == payload.email).first()

    if not record:
        raise HTTPException(status_code=404, detail="OTP not found.")
    if record.otp != payload.otp:
        raise HTTPException(status_code=400, detail="Invalid OTP.")
    if datetime.utcnow() > record.expires_at:
        raise HTTPException(status_code=400, detail="OTP expired.")

    db.delete(record)
    db.commit()

    return {"msg": "OTP verified successfully"}
