def sum(a,b):
	c=a+b
	return c
def add(a,b):
	d=a-b
	return d
def multy(a,b):
	e=a*b
	return e
def calculate(a,b,c):
	if c=="+":
		print(sum(a,b))
	elif c=="-":
		print(add(a,b))
	elif c=="*":
		print(multy(a,b))
x=int(input("enter any num:"))
y=int(input("enter second num:"))
z=input("enter operation (+,-,*,::")
calculate(x,y,z)
