lstr="""aZZg/x\ZbavpZiEZp+n)o+"""

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