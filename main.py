import requests
import os
from dotenv import load_dotenv
from send_email import send_email


load_dotenv("global.env")
API_KEY = os.getenv("API_KEY")


url = f"https://newsapi.org/v2/everything?q=tesla&\
from=2022-11-30&sortBy=publishedAt&apiKey={API_KEY}" 

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()

message = "Recent news on tesla are: \n\n\n"

for article in content["articles"]:
    if article["titile"] is not None:
        message += f"""{article["title"]} \n {article["description"]}\n\n"""
    
message = message.encode("utf-8")    
send_email(message)
