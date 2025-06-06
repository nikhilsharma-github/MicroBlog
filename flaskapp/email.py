from flask import current_app
from flask_mail import Message
from flask_babel import _
from threading import Thread
from flaskapp import mail

# Threading 
def send_async_email(app, msg):
    with app.app_context():
        mail.send(msg)


# Sending Email Method 
def send_email(subject, sender, recipients, text_body, html_body):
    msg = Message(subject, sender=sender, recipients=recipients)
    msg.body = text_body
    msg.html = html_body
    Thread(target=send_async_email, args=(current_app._get_current_object(), msg)).start()
