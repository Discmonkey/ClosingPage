import smtplib
from email.mime.text import MIMEText


class Email:

    @staticmethod
    def send(message, subject, to):
        msg = MIMEText(message)
        msg['Subject'] = subject
        msg['From'] = 'closingpage.com'
        msg['To'] = ','.join(to)

        s = smtplib.SMTP('localhost')
        s.sendmail('max@closingpage.com', to, msg.as_string())
        s.quit()
