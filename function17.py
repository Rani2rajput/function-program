def rani(a):
	i=0
	m=[]
	while i<len(a):
		if a[i]%2==0:
			m.append(a[i])
		i=i+1
	print(m)
rani([1,2,3,4,5,6,7,8,9])