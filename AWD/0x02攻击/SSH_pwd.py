#!/usr/bin/env python
#-*- coding: utf-8 -*-
import paramiko
import multiprocessing
import sys
import string
import random
class SSHD(multiprocessing.Process):
    def __init__(self,HostName,UserName,PassWord,Number):
        multiprocessing.Process.__init__(self)
        self.HostName = HostName
        self.UserName = UserName
        self.PassWord = PassWord
        self.Number = int(Number)
    def run(self):
        chars=string.ascii_letters+string.ascii_lowercase
        ResultPawwWD = "".join(random.choice(chars) for i in range(self.Number))
        print(ResultPawwWD)
        paramiko.util.log_to_file('paramiko.log')
        s=paramiko.SSHClient()
        s.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        s.connect(hostname = self.HostName,username=self.UserName, password=self.PassWord)
        print ('echo "%s" |passwd --stdin root' %ResultPawwWD)
        stdin,stdout,stderr=s.exec_command('echo %s |passwd --stdin root' %ResultPawwWD)
        print stdout.read()
        s.close()
#def GetPassWord(length=32,chars=string.ascii_letters+string.ascii_lowercase+string.punctuation):
#    return "".join(random.choice(chars) for i in range(32))
 
 
if __name__ == '__main__':
    Host = [
        ("192.168.31.143","msfadmin","admin1234"),
    ]
    for HostName,UserName,PassWord in Host:
        ssh = SSHD(HostName,UserName,PassWord,32)
        ssh.start()