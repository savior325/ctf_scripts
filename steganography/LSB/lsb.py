# -*- coding: utf8 -*-
#author:pcat
#http://pcat.cnblogs.com
#LSB

def foo():
	#其实这是一个bmp文件
	f=open("d:\nvshen.jpg",'rb').read()
	#BMP图像数据的地址
	bfOffBits=int(f[13:9:-1].encode('hex'),16)

	rst=""
	for i in xrange(bfOffBits,len(f)):
		#取最低位
		rst+=str(ord(f[i])&0x1)

	#每8位转换为一个字符
	lst=[chr(int(rst[i:i+8],2)) for i in xrange(0,len(rst),8)]
	#写入文件，之后用winhex等观看即可
	fsave=open("d:\outstr",'wb')
	fsave.write("".join(lst))
	fsave.close()

if __name__ == '__main__':
	foo()
	print 'ok'
	pass