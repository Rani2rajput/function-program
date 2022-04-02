def function(n):
	return lambda a:a*n
num=function(2)
num2=function(3)
print(num(11))
print(num2(11))