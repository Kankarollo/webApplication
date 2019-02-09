import smtplib
from email.mime.text import MIMEText


def send_email(email, height):
    from_email = "email@gmail.com"
    password_email = "Passw00rd!"
    to_email = email

    subject="height data"
    message="Hi There, you stink and your height is <strong>%s</strong>" %height

    msg = MIMEText(message, 'html')
    msg['Subject'] = subject
    msg['To'] = to_email
    msg['From']= from_email

    gmail = smtplib.SMTP('smtp.gmail.com', 587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email, password_email)
    gmail.send_message(msg)