a="udJZml2VYVuWkdxXXs2Ne1DV5V9XEs2ZdZ7WlSNbVrm9eNDSlaFXG91F"
b=a.split(" ")
s=""
for i in range(6):
	for j in b:
		if i < len(j):
			s+=j[i]
print s