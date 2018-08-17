#!/usr/bin/env python
# -*- coding: utf-8 -*-
# encode y = 3x + 13 (mod 26)
# decode x = 21(y - 12) (mod 26)
def affine(a, b):
    pwd_dic = {}
    for i in range(26):
        pwd_dic[chr(((a*i+b)%26)+0x41)] = chr(i+0x41)		# 根据实际需要，大写字母0x41，小写字母0x61
    return pwd_dic

if __name__ == '__main__':
    pwd_dic = {}
    pwd = "HIVMURCQWQIWUHEV"
    plain = []
    pwd_dic = affine(5, 8)								# 使用爆破.py求a和b
    for i in pwd:
        plain.append(pwd_dic[i])
    print "You Flag is: " + "".join(plain)
