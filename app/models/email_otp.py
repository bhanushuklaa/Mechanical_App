from sqlalchemy import Column, String, DateTime
from app.database import Base
from datetime import datetime, timedelta
import uuid

class EmailOTP(Base):
    __tablename__ = "email_otps"

    id = Column(String, primary_key=True, default=lambda: str(uuid.uuid4()))
    email = Column(String, index=True, nullable=False)
    otp = Column(String, nullable=False)
    expires_at = Column(DateTime, nullable=False, default=lambda: datetime.utcnow() + timedelta(minutes=5))
