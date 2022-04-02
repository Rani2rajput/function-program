def char(a,b):
	i=0
	while i<len(a) and i<len(b):
			if len(a)>len(b):
				print(a)
				break
			elif len(a)<len(b):
				print(b)
				break
			else:
				print(a,b)
				break
			i=i+1
char(input("enter string::"),input("enter string::"))
