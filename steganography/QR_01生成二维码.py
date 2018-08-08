# --coding:utf-8--
from PIL import Image    #kali自带包，windows需要自行下载

def foo():
	wen = open('d:/wtf.txt','rb').read()
	height = 256
	width = 256
	pic = Image.new('RGB',(width,height))
	for x in xrange(0,width):
		for y in xrange(0,height):
			if wen[x+y*256] == '0':
				pic.putpixel([x,y], 255)
			else:
				pic.putpixel([x,y], 0)
	pic.save('d:/1.png')
	pass
	
if __name__ == '__main__':      
    foo()         
    print('Done')
    pass
