import smtplib
from email.mime.text import MIMEText

# Ethereal credentials
sender_email = "filiberto35@ethereal.email"
receiver_email = "filiberto35@ethereal.email"  # send to yourself
password = "GaPCJ6WuUA9t2MZFCq"

try:
    # Create email message
    msg = MIMEText("Hello! This is a test email from Python using my new Ethereal account.")
    msg["Subject"] = "CN Assignment_02 SMTP Email"
    msg["From"] = sender_email
    msg["To"] = receiver_email

    # Connect to Ethereal SMTP server
    server = smtplib.SMTP("smtp.ethereal.email", 587)
    server.starttls()
    server.login(sender_email, password)

    # Send email
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("✅ Email sent successfully! Check Ethereal inbox.")

    server.quit()
except Exception as e:
    print("❌ Error:", e)
