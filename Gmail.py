import smtplib
server = smtplib.SMTP_SSL("smtp.gmail.com", 465)
class Gmail:

    def __init__(self,serverEmail, destinationEmail):
        self.serverEmail = serverEmail
        self.destinationEmail = destinationEmail

    def loginGmail(self, password):
        server.login(self.serverEmail, password)

    def sendEmail(self, message):
        server.sendmail(self.serverEmail, self.destinationEmail, message)

    def quit(self):
        server.quit()
