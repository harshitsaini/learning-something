# Python code to illustrate Sending mail with attachments 
# from your Gmail account  
  
# libraries to be imported 
import os
import smtplib 
from email.mime.multipart import MIMEMultipart 
from email.mime.text import MIMEText 
from email.mime.base import MIMEBase 
from email import encoders
   
fromaddr = "harshitsaini15@gmail.com"
toaddr = "sainiharshit@rocketmail.com"
   
# instance of MIMEMultipart 
msg = MIMEMultipart() 
  
# storing the senders email address   
msg['From'] = fromaddr 
  
# storing the receivers email address  
msg['To'] = toaddr 
  
# storing the subject  
msg['Subject'] = "Just testing to send attachments with a mail"
  
# string to store the body of the mail 
body = "Body_of_the_mail"
  
# attach the body with the msg instance 
msg.attach(MIMEText(body, 'plain')) 
  
# open the file to be sent  
filename = "test.txt"
attachment = open(filename, "rb") 
  
# instance of MIMEBase and named as p 
p = MIMEBase('application', 'octet-stream') 
  
# To change the payload into encoded form 
p.set_payload((attachment).read()) 
  
# encode into base64 
encoders.encode_base64(p) 
   
p.add_header('Content-Disposition', "attachment; filename= %s" % filename) 
  
# attach the instance 'p' to instance 'msg' 
msg.attach(p)
  
# creates SMTP session 
s = smtplib.SMTP('smtp.gmail.com', 587) 
  
# start TLS for security 
s.starttls() 
  
GMAIL_SMTP_USERNAME = os.getenv('GMAIL_SMTP_USERNAME')
GMAIL_SMTP_PASSWORD = os.getenv('GMAIL_SMTP_PASSWORD')

# Authentication 
s.login(GMAIL_SMTP_USERNAME, GMAIL_SMTP_PASSWORD) 
  
# Converts the Multipart msg into a string 
text = msg.as_string()

print(text)

with open("some.txt", "w+") as file:
    file.write(text)
    file.close()

text = """Content-Type: multipart/mixed; boundary="===============7576732906537280838=="
MIME-Version: 1.0
From: harshitsaini15@gmail.com
To: sainiharshit@rocketmail.com
Subject: Just testing to send attachments with a mail

--===============7576732906537280838==
Content-Type: text/plain; charset="us-ascii"
MIME-Version: 1.0
Content-Transfer-Encoding: 7bit

Body_of_the_mail
--===============7576732906537280838==
Content-Type: application/octet-stream
MIME-Version: 1.0
Content-Transfer-Encoding: base64
Content-Disposition: attachment; filename= test.txt

U29tZSB0ZXN0IGRhdGEgaW5zaWRlIHRoaXMgdGV4dCBmaWxlLgoKeG94bw==

--===============7576732906537280838==--
"""

# print(text)

# print(text)
  
# sending the mail 
s.sendmail(fromaddr, toaddr, text) 
  
# terminating the session 
s.quit() 
