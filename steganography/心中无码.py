# --coding:utf-8--

from PIL import Image
image = Image.open('d:/Lena.png')
width,height = 384,698
b0 = ''

for x in range(width):
	for y in range(height):
		if image.getpixel((x,y) ) != (255,255,0):
			if (image.getpixel((x,y) )[2] & 0x01 )== 0x01:
				b0 += '\x00\x00\x00'
			else:
				b0 += '\xff\xff\xff'

# 读取b0二维数组中元素个个数，也就是从Lena.png中读取到的像素点的个数 = len(b0)/3
pnum = len(b0)/3			
print(pnum)

# 得到像素点的个数后,可以推算出图片尺寸300x300
im = Image.frombuffer('RGB', (300,300), b0, 'raw', 'RGB', 0, 1)		
im.save('d:/1.png')
image.close()
