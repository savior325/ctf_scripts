f = open('d:/360.txt','rb')
file = f.read()
# print file

# delete the ascii char
tmp = []
for i in file:
    if( 0x7e >= ord(i) >= 0x20  ):
        continue
    else:
        tmp.append(hex(ord(i)))
# print tmp

# group the tmp chars
result = []
for j in range(0, len(tmp), 3):
    result.append( (tmp[j]+tmp[j+1]+tmp[j+2]).replace('0x','') )

# 0xe2808b -> zero-width space -> 1
# 0xe2808c -> zero-width non-joiner -> 0
# 0xe2808d -> zero-width joiner -> space
name = ''
for x in result:
    if x == 'e2808b':
        name += '1'
    elif x == 'e2808c':
        name += '0'
    elif x == 'e2808d':
        name += ' '
print name
f.close()

