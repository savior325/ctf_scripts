import subprocess
import re
import time

pattern=re.compile(r'(.*)(pts\/\d+)(.*)')
ip_list=['10.12.110.77']
#my_ip='10.12.110.77'
subprocess.Popen("who > pts.txt",shell=True)
time.sleep(0.5)
white_list_data=[]
white_list_id=[]
with open('pts.txt','r') as f:
    for i in f.readlines():
        tmp_ip_list=re.findall('\d+\.\d+\.\d+\.\d+',i)
        #print("tmp_ip_list:",tmp_ip_list)
        if len(tmp_ip_list) == 0:
            continue
        else:
            tmp_ip=tmp_ip_list[0]
            if tmp_ip in ip_list:
                data=i
                white_list_data.append(data)
#print("white_list_data:",white_list_data)
for data in white_list_data:
    id=re.findall(pattern,data)[0][1]
    #print(id)
    num=int(re.search('\d+',id).group())
    #print(num)
    white_list_id.append(num)

while True:
    try:
        for i in range(0,20):
            if i in white_list_id:
                pass
            else:
                subprocess.Popen("pkill -kill -t pts/%d 2> error.txt"%i,shell=True)
    except Exception:
        pass