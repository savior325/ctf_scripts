#!/bin/sh
# coding:utf-8
import re
flag_file = open('./flag_file.txt','a')
with open('./flag_log.log','r') as log:
	for line in log:
		if 'From :' in line:
			remote_ip = re.findall(r'(\d+\.\d+\.\d+\.\d+)', line)[0]
			flag_file.writelines(remote_ip+'\n')
		else :
			try :
				flag = re.findall(r'[a-f0-9]{32}',line)[0]
				flag_file.writelines(flag+'\n')
			except :
				pass
log.close()
flag_file.close()



