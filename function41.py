a=["rishabh","rishabh","abhishek","rishabh","divyanshu","divyanshu"]
i=0
m=[]
while i<len(a):
	if a[i] not in m:
		m.append (a[i])
	i=i+1
print(m)