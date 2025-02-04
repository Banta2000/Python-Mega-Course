import requests

# 70eaa7ba48814f049c265626844bf5cb


url = "https://newsapi.org/v2/everything?q=python&sortBy=popularity&apiKey=70eaa7ba48814f049c265626844bf5cb"


# url = ('https://newsapi.org/v2/top-headlines?'
# 'apiKey=70eaa7ba48814f049c265626844bf5cb')
# 'country=us&'

# Make the request
request = requests.get(url)

# Get the content of the response
content = request.json()

# Access the articles
articles = content["articles"]
for article in articles:
    print(article["title"])
