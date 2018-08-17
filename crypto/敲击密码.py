#coding:utf-8
import sys
mima = [['a','b','c','d','e'],['f','g','h','i','j'],['l','m','n','o','p'],['q','r','s','t','u'],['v','w','x','y','z']]
print 
if len(sys.argv)<=1:
    print "please input the code!"
    exit()
code = sys.argv[1]
for i in range(0,len(code),2):
    x = int(code[i])
    y = int(code[i+1])
    print mima[x-1][y-1],