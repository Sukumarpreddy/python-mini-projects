import smtplib
from email.message import EmailMessage

def send_email(to, subject, body):
    email = EmailMessage()
    email['From'] = 'sukumarpreddy899@gmail.com'
    email['To'] = to
    email['Subject'] = subject
    email.set_content(body)

    with smtplib.SMTP_SSL('smtp.gmail.com',465)as smtp:
        smtp.login('sukumarpreddy899@gmail.com','auuh deit arvv fvxf')
        smtp.send_message(email)
    print("✅ Email sent successfully!")

send_email('receiver@example.com','Test Subject', 'Hello, this is a test email !')