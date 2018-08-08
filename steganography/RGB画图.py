# -*- coding: utf-8 -*-
#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:     leniy_tsan
#
# Created:    10-04-2012
# Copyright:   (c) leniy_tsan 2012
# Licence:     GPL v2
#-------------------------------------------------------------------------------
#!/usr/bin/env python

from PIL import Image
import random

#98457
#x=111
#y=887

#x=887
#y=111

#78400
x=280
y=280

c = Image.new("RGB",(x,y))


f = open("hint2.txt", "r")

for i in range (0,x):
    for j in range (0,y):
       #读一行，写一个像素
       line = f.readline()
       r1=int(line.split(',')[0])
       g1=int(line.split(',')[1])
       b1=int(line.split(',')[2])
       #c.putpixel([i,j],(random.randint(0,255),random.randint(0,255),random.randint(0,255)))
       c.putpixel([i,j],(r1,g1,b1))

c.save("hint2.jpg")
f.closed

#c.show()


'''
line = f.readline()
#print line

r1=line.split(',')[0]
g1=line.split(',')[1]
b1=line.split(',')[2]
print r1,g1,b1

line = f.readline()
#print line
r1=line.split(',')[0]
g1=line.split(',')[1]
b1=line.split(',')[2]
print r1,g1,b1
'''