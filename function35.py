def function():
	i=1
	while i<=1000:
		print(i)
		if i%3==0:
			print("nav",i)
		elif i%7==0:
			print("gurukul",i)
		elif i%21==0:
			print("navgurukul",i)
		i=i+1
function()