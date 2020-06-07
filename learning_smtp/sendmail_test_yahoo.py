# Python code to illustrate Sending mail from  
# your yahoo account  
import smtplib 
  
# creates SMTP session 
s = smtplib.SMTP('smtp.mail.yahoo.com', 587) 
  
# start TLS for security 
s.starttls() 

GMAIL_SMTP_USERNAME = os.getenv('GMAIL_SMTP_USERNAME')
GMAIL_SMTP_PASSWORD = os.getenv('GMAIL_SMTP_PASSWORD')
  
# Authentication 
s.login("sender_email_id", "sender_email_id_password") 
  
# message to be sent 
message = "Message_you_need_to_send"
  
# sending the mail 
s.sendmail("sender_email_id", "receiver_email_id", message) 
  
# terminating the session 
s.quit() 
