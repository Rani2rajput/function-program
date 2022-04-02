def function():
	a=input("enter strong number::")
	if len(a)>=6 and len(a)<=16 and "@" in a or "$" in a and "A" in a or "Z" in a and "a" in a or "z" in a and "2" in a or "8"in a:
		print("strong password")
	else:
		print("week password")
function()