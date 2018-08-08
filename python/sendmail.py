#!/usr/bin/python
#-*- coding:utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from email.header import Header

def sendmail(text):
    mail_host = "smtp.xxx.com"  #设置服务器
    mail_user = "******"  #设置用户名
    mail_pass = "******"  #设置口令

    sender = "****@xxx.com"    #设置发件人,必须和mail_user一致
    receivers = ['****@xxx.com']    #收件人邮箱

    message = MIMEText(text, 'plain', 'utf-8')
    subject = 'what u want'
    message['Subject'] = Header(subject, 'utf-8')     #设置邮件主题

    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)  #连接smtp服务器，端口号25
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print "已发送邮件至******！"
    
if __name__ == '__main__':
	sendmail('helloworld')
