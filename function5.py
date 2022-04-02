def eligible(user):
	if user>=18:
		print("eligible for vote")
	else:
		print("not eligible")
a=int(input("enter age::"))	
eligible(a)