#  -*- coding: utf-8 -*-

import requests
import time

#print "downloading with requests"

#cookie = {'PHPSESSID': '47lkngj51t80judh97q1dl4jmoimpplq'}#传递cookie

def downloadflag(url1):
    cookies={'sessionid':'cq1qsz9ppif5mk1n115dl7wfdn7ozgvt'}

    bd_session=requests.session()

    r=bd_session.get(url1,cookies={'sessionid': 'cq1qsz9ppif5mk1n115dl7wfdn7ozgvt'})

    #with open(swfdir+'/'+swfnumber+".swf", "wb") as code:
        #code.write(r.content)
    data=r.content

    bd_session.close()

    return data

#172.20.115.101
#172.20.115.102


ipaddressStart=86
ipaddressStop=86
flagposition='/flag1.txt'


filename=time.strftime('%Y-%m-%d-%H-%M-%S',time.localtime(time.time()))

filelog=open('./data/'+filename+'.txt', "wb")

iprangge=[101,102]

for j in range(100,131):
    ipaddressC='172.20.'
#for i in range(ipaddressStart,ipaddressStop+1):
    for i in iprangge:
        ipaddress=ipaddressC+str(j)+'.'
        ipaddress=ipaddress+str(i)
        #print 'ipaddress=',ipaddress
        url='http://'+ipaddress+flagposition
        print 'url=',url

        #result=downloadflag(url)
        #print 'result=',result

        # result=ipaddress+','+url+','+result
        #print result

        #if '404' not in result:
        #    filelog.write(result)

filelog.close()













