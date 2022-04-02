def function(a):
	print(a)
	if a==1:
		return 1
	return function(a-1)
function(5)