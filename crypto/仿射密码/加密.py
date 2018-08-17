#coding:utf-8
def affine(a,b,str):
    for i in str:
        print chr(((a*(ord(i)-65)+b)%26)+65),
if __name__ == '__main__':
    str = 'FANGSHEMIMAISFUN'
    affine(5,8,str)
	