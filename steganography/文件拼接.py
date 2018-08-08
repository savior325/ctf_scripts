f1 = open('D:/flyflys/1.bin','rb').read()
f2 = open('D:/flyflys/2.bin','rb').read()
f3 = open('D:/flyflys/3.bin','rb').read()
f4 = open('D:/flyflys/4.bin','rb').read()
f5 = open('D:/flyflys/5.bin','rb').read()

size = 525701
offset = ( len(f1) + len(f2) + len(f3) + len(f4) + len(f5) - size ) / 5

fly = open('d:/flyflys/fly.rar','wb')
fly.write(f1[offset:] + f2[offset:] + f3[offset:] + f4[offset:] + f5[offset:])
fly.close()


