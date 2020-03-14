#https://www.tutorialspoint.com/send-mail-from-your-gmail-account-using-python

import smtplib
from os.path import basename
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication

mail_content = '''Hello,
This is a simple mail. There is only text, no attachments are there The mail is sent using Python SMTP library.
Thank You
'''
#The mail addresses and password
sender_address = 'nghiahsgs40@gmail.com'
sender_pass = 'Nguyenngocyen97@'
receiver_address = 'nghiahsgs@gmail.com'

#Setup the MIME
message = MIMEMultipart()
message['From'] = sender_address
message['To'] = receiver_address
message['Subject'] = 'A test mail sent by Python. It has an attachment.2'   #The subject line
#The body and the attachments for the mail
message.attach(MIMEText(mail_content, 'plain'))

#attach file 
# for f in files or []:
f = 'letters/letters0.pdf'
with open(f, "rb") as fil:
    part = MIMEApplication(
        fil.read(),
        Name=basename(f)
    )
# After the file is closed
part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
print(basename(f))
message.attach(part)

#Create SMTP session for sending the mail
session = smtplib.SMTP('smtp.gmail.com', 587) #use gmail with port
session.starttls() #enable security
session.login(sender_address, sender_pass) #login with mail_id and password
text = message.as_string()
session.sendmail(sender_address, receiver_address, text)
session.quit()
print('Mail Sent')
