# coding:utf-8

import requests
import base64


url = 'http://ctf5.shiyanbar.com/web/10/10.php'
r = requests.get(url)
flag = base64.b64decode(r.headers['FLAG'])
print( flag.split(':')[1]) 

data1 = {
	'key': flag.split(':')[1]
}
r1 = requests.post('http://ctf5.shiyanbar.com/web/10/10.php', data=data1)
print(r1.content)
