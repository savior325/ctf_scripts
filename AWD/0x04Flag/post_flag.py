#!/usr/bin/env python2
#coding:utf-8
import requests
import re

def submit(remote_ip, flag):
    team_token = "MW4wa0pVZUFSbEU0WmR4TzlnUWhwL3lkNHZ0WUdmUjdlYU5r"
    url = '10.10.0.2:80/sumbit-flag'
    if not team_token or not flag:
        raise Exception('team token or flag not found')
    try :
        conn = requests.get(url, timeout=3)
    except :
        print "Connection ERROR!"
    data = {
        'ip': remote_ip,
        'flag': flag,
        'token': team_token
    }
    headers = {
        "Content-type": "application/x-www-form-urlencoded"
    }
    # res = requests.post(url, data=data, headers=headers, timeout=2)
    res = requests.post(url, data=data, timeout=2)
    if "success" in res.text:
        return True
    else:
        return False
    

if __name__ == '__main__':
    file = open('./flag.txt','r')
    i = 1
    for line in file:
        try :
            ip = re.findall(r'(\d+\.\d+\.\d+\.\d+)',line)[0]
            flag = re.findall(r'flag{(.*)}',line)[0]
            i++
            if submit(remote_ip=ip, flag=flag):
                print "%s  WITH  %s sumbit success!"%(ip,flag)
            else:
                print "%s  WITH  %s sumbit Failed!"%(ip,flag)
        except :
            print "Can't find any flag in line : %d"%i
            continue
        