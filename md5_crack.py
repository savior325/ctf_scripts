import hashlib
import time
# md5 : 38e4c352809e150186920aac37190cbc
# flag: flag{www_shiyanbar_com_is_very_good_????}

a = '38e4c352809e150186920aac37190cbc'
dic = r"0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&()*+,-./:;<=>?@[\]^_`{|}~ "
# dic = r"0123456789abcdefghijklmnopqrstuvwxy"

print (time.localtime())
for i1 in dic:
    for i2 in dic:
        for i3 in dic:
            for i4 in dic:
                md5 = hashlib.md5()
                b = 'flag{www_shiyanbar_com_is_very_good_' +i1+i2+i3+i4+ '}'
                md5.update(b)
                # print md5.hexdigest()
                if md5.hexdigest() == a:
                    print '%s  %s %s' %(md5.hexdigest(),b,time.localtime())                                    
print ("NULL",time.localtime())