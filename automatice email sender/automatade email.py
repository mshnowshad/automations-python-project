import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, receiver_email, subject, body, smtp_server, smtp_port, smtp_username, smtp_password):
    # Set up the MIME
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = subject

    # Attach the message body
    message.attach(MIMEText(body, 'plain'))

    # Connect to the SMTP server
    with smtplib.SMTP(smtp_server, smtp_port) as server:
        # Log in to the SMTP server
        server.starttls()
        server.login(smtp_username, smtp_password)

        # Send the email
        server.sendmail(sender_email, receiver_email, message.as_string())

# Example usage
sender_email = "nowshedahmed59@gmail.com"
receiver_email = input('enter the receiver username: ')
subject = input('enter the subject: ')
body = input('enter the body: ')
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "nowshedahmed59@gmail.com"
smtp_password = "pqkwshklqycypzyc"
# depp8660@gmail.com
send_email(sender_email, receiver_email, subject, body, smtp_server, smtp_port, smtp_username, smtp_password)



# https://security.google.com/settings/security/apppasswords
 # apppassword create kore passkey ta use korthe hoy...