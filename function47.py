def function():
	a=[3,4,5,0,2,0,9,0]
	i=0
	m=[]
	l=[]
	while i<len(a):
		if a[i]==0:
			m.append(a[i])
		else:
			l.append(a[i])
		i=i+1
	j=0
	while j<len(m):
		l.append(m[j])
		j=j+1
	print(l)
function()
