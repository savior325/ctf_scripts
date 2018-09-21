import sys,subprocess,re,time

if __name__ == '__main__':
	if len(sys.argv) != 2:
		print "Usage:  python kill.py [your IP]"
		exit(1)
	my_ip = sys.argv[1]

	while True:
		subprocess.Popen("netstat -anultp > net.txt 2>/dev/null",shell=True)
		time.sleep(0.5)

		file = open("net.txt","r")
		for line in file:
			if re.search(r'.*'+my_ip+':.*',line)==None:
				try :
					pid = re.findall(r'(\d+)\/\S+',line)[0]
					addr = re.findall(r'(\d+\.\d+\.\d+\.\d+:\d+)',line)[1]
					subprocess.Popen("kill -9 %s"%pid,shell=True)
					print "pid %s has been killed! Remote address is %s"%(pid,addr)
				except :
					pass

		time.sleep(3)
