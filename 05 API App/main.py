import requests
import smtplib, ssl
import io
import sys
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


# 70eaa7ba48814f049c265626844bf5cb


def send_email(message):
    host = "smtp.gmail.com"
    port = 465

    username = "manuel.altermatt@gmail.com"
    password = "qgpd okcn kbum ptlr"

    receiver = "manuel.altermatt@gmail.com"

    context = ssl.create_default_context()

    with smtplib.SMTP_SSL(host, port, context=context) as server:
        server.login(username, password)
        server.sendmail(username, receiver, message)


url = "https://newsapi.org/v2/everything?q=python&sortBy=popularity&apiKey=70eaa7ba48814f049c265626844bf5cb"


# url = ('https://newsapi.org/v2/top-headlines?'
# 'apiKey=70eaa7ba48814f049c265626844bf5cb')
# 'country=us&'

# Make the request
request = requests.get(url)

# Get the content of the response
content = request.json()

# Access the top 10 articles
articles = content["articles"][:10]


# Create a message made of the top articles
message = """Top Headlines\n\n"""

for article in articles:
    message += f"{article['title']}\n"
    # print(article["publishedAt"])


# Send the email
send_email(message)

# article
# source
# author
# title
# description
# url
# content
# Set the encoding to utf-8
