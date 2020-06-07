#!/usr/bin/python

import os
import smtplib

sender = 'test@harshitsaini.me'
receivers = ['ok@harshitsaini.me',
             'harshitsaini15@gmail.com',
             # 'sainiharshit@rocketmail.com'
             ]

message = """From: From Person <harshitsaini15@gmail.com>
To: <sainiharshit@rocketmail.com>,<harshitsaini15@gmail.com>
Subject: SMTP e-mail test

This is a test e-mail message.
"""

username = os.getenv("SMTP_USERNAME")
password = os.getenv("SMTP_PASSWORD")

try:
   print("Starting SMTP connection")
   smtpObj = smtplib.SMTP('email-smtp.us-east-1.amazonaws.com', 467)
   print("SMTP connection established")
   _, res = smtpObj.starttls()
   print(res)
   smtpObj.login(username, password)
   print("SMTP authentication complete")
   res = smtpObj.sendmail(sender, receivers, message)         
   print(res)
   print("Successfully sent email")
except SMTPException:
   print("Error: unable to send email")
