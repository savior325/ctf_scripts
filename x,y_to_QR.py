#-*- coding: UTF-8 -*-
import re
import matplotlib.pyplot as plt 
# 需要kali环境，坐标文件内容格式：(178,114)

f = open(r'1.txt', 'r+')
string = f.read()

# 正则表达式
patternX = '\((\d+),'
patternY = ',(\d+)\)'
 
# 使用Pattern匹配文本，获得匹配结果，无法匹配时将返回None
matchX = re.findall(patternX, string, re.M)
matchY = re.findall(patternY, string, re.M)


#转为int列表
matchX = [ int(x) for x in matchX ]
matchY = [ int(y) for y in matchY ]



#plt.plot(matchX,matchY) 
plt.scatter(matchX,matchY) 

plt.show()  