# Python code to illustrate Sending mail from
# your Gmail account
import os
import smtplib

# creates SMTP session
s = smtplib.SMTP('smtp.gmail.com', 587)

# start TLS for security
s.starttls()

GMAIL_SMTP_USERNAME = os.getenv('GMAIL_SMTP_USERNAME')
GMAIL_SMTP_PASSWORD = os.getenv('GMAIL_SMTP_PASSWORD')


# print(GMAIL_SMTP_USERNAME, GMAIL_SMTP_PASSWORD)


# Authentication
s.login(GMAIL_SMTP_USERNAME, GMAIL_SMTP_PASSWORD)

# message to be sent
message = "Message_you_need_to_send"

# sending the mail
s.sendmail("harshitsaini15@gmail.com",
           ["test@harshitsaini.me", "sainiharshit@rocketmail.com"],
           message)

# terminating the session
s.quit()
