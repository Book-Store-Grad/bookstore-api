import yagmail


class SendEmail:
    def __init__(self, email, password):
        self.email = email
        self.password = password

    def send_email(self, to, subject, contents):
        try:
            # initiating connection with SMTP server
            yag = yagmail.SMTP(self.email, self.password)

            # Adding multiple attachments and mailing them
            yag.send(to, subject, contents, )
            print("Email sent successfully")
        except Exception as e:
            print("Error: unable to send email")
            print(e)
            return False
        return True
