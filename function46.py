a="my name is priya"
i=0
b=[]
while i<len(a):
	if a[i]!=0:
		b.append(ord(a[i]))
	else:
		pass
	i=i+1
print(b)