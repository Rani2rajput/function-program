def function(a,b):
	i=0
	m=[]
	while i<len(a):
		if a[i] not in m:
			m.append(a[i])
		i+=1
	j=0
	n=[]
	while j<len(b):
		if b[j] not in n:
			n.append(b[j])
		j=j+1
	print(m,n)
function([1,2,3,3,3,6,3,6,6,7,4,5],[1,2,3,4,5])
