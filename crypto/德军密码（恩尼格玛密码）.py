str_bin='0000011000000000101010110111001011000101100000111001100100111100111001'
str_key='helloworld'
list_bin=[]
#print str_bin[0:7]
for i in range(10):
    list_bin.append(str_bin[7*i:7*i+7])
for i in range(len(str_key)):
    print chr(int(list_bin[i],2) ^ ord(str_key[i])),