import os 
from dotenv import load_dotenv
import smtplib, ssl

load_dotenv("global.env")
USERNAME = os.getenv("EMAIL_USERNAME")
PASSWORD = os.getenv("EMAIL_PASS")

HOST = "smtp.gmail.com"
PORT = 465

reciver = USERNAME

def send_email(message):
    
    context = ssl.create_default_context()
    
    with smtplib.SMTP_SSL(HOST, PORT, context=context) as server:
        server.login(USERNAME, PASSWORD)
        server.sendmail(USERNAME, reciver, message)