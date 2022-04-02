a=int(input("enter a number:"))
def function():
	i=0
	while i<=a:
		num=int(input("enter the num:"))
		if num%3==0 and num%5==0:
			print("fizz-buzz")
		elif num%3==0:
			print("fizz")
		elif num%5==0:
			print("buzz")
		else:
			print("buzz_fizz")
		i=i+1
function()