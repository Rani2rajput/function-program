def perfect(p):
	i=1
	while i<=p:
		n=i
		sum=0
		m=1
		while m<i:
			if n%m==0:
				sum=sum+m
			m=m+1
		if sum==n:
			print("perfect",n)
		i=i+1 
		p+=1
num=int(input("enter any num:"))
perfect(num)