#!/usr/bin/python

import os
import smtplib
import base64

filename = "test.txt"

# Read a file and encode it into base64 format
fo = open(filename, "rb")
filecontent = fo.read()
encodedcontent = base64.b64encode(filecontent)  # base64


sender = 'test@harshitsaini.me'
receivers = ['some@harshitsaini.me',
             'harshitsaini15@gmail.com',
             # 'sainiharshit@rocketmail.com'
             ]

# message = """From: From Person <harshitsaini15@gmail.com>
# To: <sainiharshit@rocketmail.com>,<harshitsaini15@gmail.com>
# Subject: SMTP e-mail test

# This is a test e-mail message.
# """

username = os.getenv("SMTP_USERNAME")
password = os.getenv("SMTP_PASSWORD")

test_message = """Content-Type: multipart/mixed; boundary="===============0731916686213514151=="
MIME-Version: 1.0
From: test@harshitsaini.me
To: harshitsaini15@gmail.com
Subject: Just testing to send attachments with a mail

--===============0731916686213514151==
Content-Type: text/plain; charset="us-ascii"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit

Body_of_the_mail
--===============0731916686213514151==
Content-Type: application/octet-stream
MIME-Version: 1.0
Content-Transfer-Encoding: base64
Content-Disposition: attachment; filename= test.txt

U29tZSB0ZXN0IGRhdGEgaW5zaWRlIHRoaXMgdGV4dCBmaWxlLgoKeG94bw==

--===============0731916686213514151==--
"""


# marker = "AUNIQUEMARKER"
marker = "===============0731916686213514151=="

body ="""
This is a test email to send an attachement.
"""
# Define the main headers.
part1 = """
Content-Type: multipart/mixed; boundary="%s"
MIME-Version: 1.0
From: test@harshitsaini.me
To: some@harshitsaini.me,harshitsaini15@gmail.com
Subject: Sending Attachement

--%s
""" % (marker, marker)

# Define the message action
part2 = """Content-Type: text/plain; charset="us-ascii"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit

%s
--%s
""" % (body,marker)

# Define the attachment section
part3 = """Content-Type: text/plain; name="test.txt"
Content-Description: test.txt
Content-Disposition: attachment;filename="%s";
    creation-date="Sat, 05 Aug 2017 19:35:36 GMT";
Content-Transfer-Encoding: base64

%s
--%s--
""" %(filename, encodedcontent.decode(), marker)
message = part1 + part2 + part3



# from email.mime.text import MIMEText
# from email.mime.multipart import MIMEMultipart


# msg = MIMEMultipart()
# msg['Subject'] = "test subject"
# msg['From'] = "test@harshitsaini.me"
# msg['To'] = ", ".join(receivers)

# # Record the MIME types of both parts - text/plain and text/html.
# # utf-8 -> https://stackoverflow.com/questions/5910104/python-how-to-send-utf-8-e-mail#5910530
# part1 = MIMEText(filecontent, 'plain', "utf-8")
# part2 = MIMEText(encodedcontent, 'html', "utf-8")

# msg.attach(part1)
# msg.attach(part2)

# message = msg.as_string()


print(message)



try:
   print("Starting SMTP connection")
   # SMTP_URL = 'email-smtp.us-east-1.amazonaws.com'
   # SMTP_PORT = 587
   SMTP_URL = "localhost"
   SMTP_PORT = 1025
   smtpObj = smtplib.SMTP(SMTP_URL, SMTP_PORT)
   print("SMTP connection established")
   # _, res = smtpObj.starttls()
   # print(res)
   # smtpObj.login(username, password)
   # print("SMTP authentication complete")
   res = smtpObj.sendmail(sender, receivers, test_message)         
   print(res)
   print("Successfully sent email")
except Exception:
   print("Error: unable to send email")
   raise



