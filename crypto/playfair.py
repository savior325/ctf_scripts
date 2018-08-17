# --coding:utf-8--

from pycipher import Playfair

# 首先自己根据tips或密钥编制密码表
# attention:可能会有X补位
encode = Playfair('CULTREABDFGHIKMNOPQSVWXYZ').encipher('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG')
decode = Playfair('CULTREABDFGHIKMNOPQSVWXYZ').decipher('UKDNLHTGFLWUSEPWHLISNPCGCRGAUBVZAQIV')
print('encode:' + encode)
print('decode:' + decode)