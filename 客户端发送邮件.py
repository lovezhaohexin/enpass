#!/usr/bin/env python3
import smtplib
import getpass
from email.mime.text import  MIMEText
from email.header import Header

def send_email(text,sender,receivers,subject,host,user,passwd):


    message = MIMEText('Python3 email test.\r\n','plain','utf8')
    message['FROM'] = Header(sender,'utf8')
    message['To'] = Header(receivers[0],'utf8')
    message['Subject'] = Header(subject,'utf8')

    smtp = smtplib.SMTP(host)
    smtp.login(user,passwd)
    smtp.sendmail(sender,receivers,message.as_bytes())


if __name__ == '__main__':
    text = '这是一封python邮件测试\r\n'
    sender = 'e_l_kibana@163.com'

    recerivers = ['3229034427@qq.com']
    subject = 'hello xinxin'
    host = 'smtp.163.com'
    user = 'e_l_kibana@163.com'
    passwd = getpass.getpass()
    send_email(text,sender,recerivers,subject,host,user,passwd)










