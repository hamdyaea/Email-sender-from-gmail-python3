#!/usr/bin/env python3

# Developer : Hamdy Abou El Anein
# hamdy.aea@protonmail.com


import smtplib


class Mailer:
    def __init__(self):
        self.fromaddr
        self.toaddrs
        self.msg


Mailer.fromaddr = "fromuser@gmail.com"
Mailer.toaddrs = "touser@gmail.com"
Mailer.msg = "There was a terrible error that occured and I wanted you to know!"


# Credentials (if needed)
username = "username"
password = "password"

# The actual mail send
server = smtplib.SMTP("smtp.gmail.com:587")
server.starttls()
server.login(username, password)
server.sendmail(Mailer.fromaddr, Mailer.toaddrs, Mailer.msg)
server.quit()
