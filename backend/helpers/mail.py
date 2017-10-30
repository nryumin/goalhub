from smtplib import SMTP_SSL as SMTP
from email.mime.text import MIMEText
from email.header import Header


gmail_user = 'vinni.ze.puh@gmail.com'
gmail_password = 'vinnizepuh120390'


def sendMail(reciever,subject,text):
    server = SMTP('smtp.gmail.com', '465')
    server.ehlo()
    server.login(gmail_user, gmail_password)

    subject = subject
    body = text
    msg = MIMEText(body, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')
    server.sendmail(gmail_user, reciever, msg.as_string())