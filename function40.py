a=int(input("enter your num1:"))
b=int(input("enter your num2:"))
c=int(input("enter your num3:"))
def function():
	if a>b and b>c:
		print("maximum num:",a)
	elif b>a and b>c:
		print("maximum num:",b)
	elif c>a and c>b:
		print("maximum num",c)
function()