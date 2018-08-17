# --coding:utf-8--

from pycipher import Vigenere

# 首先自己根据tips或密钥编制密码表
encode = Vigenere('CULTURE').encipher('THE QUICK BROWN FOX JUMPS OVER THE LAZY DOG')
decode = Vigenere('CULTURE').decipher('VBPJOZGMVCHQEJQRUNGGWQPPKNYINUKRXFK')
print('encode:' + encode)
print('decode:' + decode)