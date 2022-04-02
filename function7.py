a=int(input("enter number::"))
def even():
	i=0
	while i<=a:
		if i%2==0:
			print("even",i)
		else:
			print("odd",i)
		i=i+1
even()