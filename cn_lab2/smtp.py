import smtplib
from email.mime.text import MIMEText

def send_email():
    sender = "hello@demomailtrap.co"       # Must be a valid email
    receiver = "saicharan.g07@gmail.com"     # Your Mailtrap inbox
    username = "api"
    password = "b13f5c0b6bc3d421a53f6adb799677c1"

    msg = MIMEText("Hello Siddhartha, this is a test email via Mailtrap.")
    msg["Subject"] = "CN Lab 2 - SMTP Test"
    msg["From"] = sender
    msg["To"] = receiver

    try:
        s = smtplib.SMTP("live.smtp.mailtrap.io", 587)
        s.starttls()
        s.login(username, password)
        s.sendmail(sender, receiver, msg.as_string())
        s.quit()
        print("Email sent successfully. Check your Mailtrap inbox!")
    except Exception as e:
        print("Error:", e)

send_email()

