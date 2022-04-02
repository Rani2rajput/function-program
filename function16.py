def unique(a,b):

	i=0
	m=[]
	while i<len(a) and i<len(b):
		if a[i] not in b:
			m.append(a[i])
		if b[i] not in a:
			m.append(b[i])
		i=i+1
	print(m)
unique([2,4,5,6,7,8],[1,6,8,9,5,4])