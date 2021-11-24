import smtplib
import ssl

from API import *

port = 587  # For starttls
smtp_server = "smtp.gmail.com"
sender_email = "sender_email@gmail.com"
receiver_email = "receiver_email@gmail.com"
# password = input("Type your password and press enter:")
message = """\
Subject: Greetings

Hope that you are well.
Regards
Maruf Billah."""


def sendEmail():
    context = ssl.create_default_context()
    with smtplib.SMTP(smtp_server, port) as server:
        server.ehlo()  # Can be omitted
        server.starttls(context=context)
        server.ehlo()  # Can be omitted
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, message)

# sendEmail()
