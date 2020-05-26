import smtplib
from email.mime.text import MIMEText

def send_email(email,height,avg_height,count):

    from_email="ashishchaturvedi1991@gmail.com"
    from_password = ""
    to_email = email

    subject = "Height Data"
    message = "Hey there, Your height is <strong>%s</strong>.<br>Average height of all is <strong>%s</strong> out of <strong>%s</strong> people.<br>Thanks! " %height %avg_height %count

    msg = MIMEText(message,"html")
    msg["Subject"]=subject
    msg["To"]=to_email
    msg["From"]=from_email

    gmail=smtplib.SMTP("smtp.gmail.com",587)
    gmail.ehlo()
    gmail.starttls()
    gmail.login(from_email,from_password)
    gmail.send_message(msg)
