# import orm,asyncio,sys
# from models import User, Blog, Comment

# def test(loop):
#     yield from orm.create_pool(loop=loop, user='root', password='password', db='awesome')

#     u = User(name='Test', email='test@example.com', passwd='1234567890', image='about:blank')

#     yield from u.save()

# if __name__ == '__main__':

#     loop = asyncio.get_event_loop()
#     loop.run_until_complete( asyncio.wait([test( loop )]) )  
#     loop.close()
#     if loop.is_closed():
#         sys.exit(0)
# class student(object):
#     def __init__(self,name,score):
#         self.name=name
#         self.score=score

#     def print(self):
#         print('%s:%s' % (self.name,self.score))

# if __name__ == '__main__':
#     bart=student('xsc',55)
#     bart.print()
from email import encoders
from email.header import Header
from email.mime.text import MIMEText
from email.utils import parseaddr, formataddr
import smtplib

def _format_addr(s):
    name, addr = parseaddr(s)
    return formataddr((Header(name, 'utf-8').encode(), addr))

from_addr = input('From: ')
password = input('Password: ')
to_addr = input('To: ')
smtp_server = input('SMTP server:')

msg = MIMEText('hello, send by Python...', 'plain', 'utf-8')
msg['From'] = _format_addr('Python爱好者 <%s>' % from_addr)
msg['To'] = _format_addr('管理员 <%s>' % to_addr)
msg['Subject'] = Header('来自SMTP的问候……', 'utf-8').encode()

# server = smtplib.SMTP(smtp_server, 25)
server = smtplib.SMTP_SSL(smtp_server, 465)
server.set_debuglevel(1)
server.login(from_addr, password)
server.sendmail(from_addr, [to_addr], msg.as_string())
server.quit()