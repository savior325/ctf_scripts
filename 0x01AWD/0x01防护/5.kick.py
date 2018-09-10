# please define your ip: my_ip

import subprocess
import re

pattern=re.compile(r'(.*)(pts\/\d+)(.*)')
my_ip='10.12.110.102'
subprocess.Popen("w > pts.txt",shell=True)
with open('pts.txt','r') as f:
    for i in f.readlines():
        if my_ip in i:
            data=i
            break

id=re.findall(pattern,data)[0][1]
num=int(re.search('\d+',id).group())
while True:
    try:
        for i in range(2,20):
            if i==num:
                pass
            else:
                subprocess.Popen("pkill -kill -t pts/%d 2> error.txt"%i,shell=True)
    except Exception:
        pass