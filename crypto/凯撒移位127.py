lstr="""e6ece1e7fbb8b4b5e2e6b9e5b7e3e6e4e4b8b5e5b8b7e3b3b5b8b6b7b3b5e1e1e4e5e6e4b1fd"""

for p in range(127):
	str1 = ''
	for i in lstr:
		temp = chr((ord(i)+p)%127)
		if 32<ord(temp)<127 :			# ascii ONLY 32-127 can output
			str1 = str1 + temp 
			feel = 1
		else:
			feel = 0
			break
	if feel == 1:
		print(str1)