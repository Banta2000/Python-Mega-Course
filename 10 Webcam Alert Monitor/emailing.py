import smtplib
from email.message import EmailMessage

sender = "manuel.altermatt@gmail.com"
password = "qgpd okcn kbum ptlr"
receiver = "manuel.altermatt@gmail.com"


def send_email(img_path):
    email_message = EmailMessage()
    email_message["Subject"] = "Motion Detected"
    email_message.set_content("Motion Detected in your area. Please check the attached image.")

    with open(img_path, "rb") as f:
        content = f.read()

    email_message.add_attachment(content, maintype="image", subtype="jpeg", filename=f.name)

    gmail = smtplib.SMTP("smtp.gmail.com", 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(sender, password)
    gmail.sendmail(sender, receiver, email_message.as_string())


if __name__ == "__main__":
    send_email("images/17frame.jpg")
