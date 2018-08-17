#coding:utf-8
'''
A(0):I(8)
B(1):N(13)
Y:y
Z:D
'''

a=1
for a in range(1,26):
    for b in range(26):
        if ((0*a+b)%26 == 8)and((1*a+b)%26 == 13):
            print "a:"+str(a)+","+"b:"+str(b)
            break