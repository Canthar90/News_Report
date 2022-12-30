import requests
import os
from dotenv import load_dotenv
from send_email import send_email
import datetime as dt


load_dotenv("global.env")
API_KEY = os.getenv("API_KEY")

today = dt.date.today()
month_ago = today - dt.timedelta(days=30)
month_ago = month_ago.strftime("%Y-%m-%d")


url = f"https://newsapi.org/v2/everything?q=tesla&\
from={month_ago}&sortBy=publishedAt&apiKey={API_KEY}&language=en" 

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

message = "Subject: Recent news on tesla are:\n"

for article in content["articles"][:20]:
    if article["title"] is not None:
        message += f"""{article["title"]} \n \
            {article["description"]}\n {article["url"]} \n\n"""
    
message = message.encode("utf-8")    
send_email(message)
