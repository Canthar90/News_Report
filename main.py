import requests
import os
from dotenv import load_dotenv


load_dotenv("global.env")
API_KEY = os.getenv("API_KEY")


url = f"https://newsapi.org/v2/everything?q=tesla&\
from=2022-11-30&sortBy=publishedAt&apiKey={API_KEY}" 

# Make request
request = requests.get(url)

# Get a dictionary with data
content = request.json()


for article in content["articles"]:
    print(article["title"])
    print(article["description"])