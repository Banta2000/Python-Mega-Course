import smtplib, ssl

host = "smtp.gmail.com"
port = 465

username = "manuel.altermatt@gmail.com"
password = "qgpd okcn kbum ptlr"

receiver = "manuel.altermatt@gmail.com"

message = """"\
Subject: OPEN ME
Hi, this is an importa mail.
"""

context = ssl.create_default_context()

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)
