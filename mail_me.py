import smtplib


class mail_man():
    def __init__(self,to,body):

        self.subject = 'Type your subject here'
        self.body = body
        self.to = to





        self.server = smtplib.SMTP('smtp.gmail.com',587)
        self.server.ehlo()
        self.server.starttls()
        self.server.ehlo()

        self.server.login('type sending email here','type key here')

        self.msg = f'Subject: {self.subject}\n\n{self.body}'

        self.server.sendmail(
            'type sending email here',
             self.to,
             self.msg
        )
        print('finished')




if __name__ == '__main__':
    mm = mail_man(body= 'testing',to='type receiving email here')
