# coding=utf-8

'''

<html>
    <head>
        <meta http-equiv=Content-Type content="text/html;charset=utf-8">
    </head>
    <body>
       
        <form action="" method="post">
            请在2秒内口算结果并提交！<br/>
            6630*11586+1309*(6630+11586)=<input type="text" name="v"/>
            <input type="submit" value="提交"/>
        </form>
    </body>
</html>

'''

import requests
import re
# get the page
s = requests.Session()
url = 'http://lab1.xseclab.com/xss2_0d557e6d2a4ac08b749b61473a075be1/index.php'
req = s.get(url)
print(req.content)

# get the equation
num = re.findall(r'<br/>\s+(.*?)=', req.content)[0]
print("请计算："+num)

# calc the result and post
post1 = {'v': eval(num)}
req1 = s.post(url, data=post1)
print(req1.content)



