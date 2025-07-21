import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os
from dotenv import load_dotenv

load_dotenv()  

EMAIL_HOST = os.getenv("EMAIL_HOST", "smtp.gmail.com")
EMAIL_PORT = int(os.getenv("EMAIL_PORT", 587))  # Default to TLS
EMAIL_USERNAME = os.getenv("EMAIL_USERNAME")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")

def send_email_otp(to_email: str, otp: str) -> bool:
    """
    Sends OTP email to the given recipient.

    Args:
        to_email (str): Recipient email address
        otp (str): OTP code

    Returns:
        bool: True if sent successfully, False otherwise
    """
    subject = "Your OTP Code"
    body = f"Your OTP is: {otp}\n\nIt is valid for 5 minutes. Do not share this code."

    msg = MIMEMultipart()
    msg["From"] = EMAIL_USERNAME
    msg["To"] = to_email
    msg["Subject"] = subject
    msg.attach(MIMEText(body, "plain"))

    try:
        with smtplib.SMTP(EMAIL_HOST, EMAIL_PORT) as server:
            server.starttls()
            server.login(EMAIL_USERNAME, EMAIL_PASSWORD)
            server.sendmail(EMAIL_USERNAME, to_email, msg.as_string())
        return True
    except smtplib.SMTPAuthenticationError:
        print("SMTP Authentication Error: Check EMAIL_USERNAME or EMAIL_PASSWORD (possibly use App Password)")
    except Exception as e:
        print(f"Failed to send email: {e}")
    return False
