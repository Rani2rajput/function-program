speed=int(input("entet speed::"))
def function():
	point=(speed-70)//5
	if speed<=70:
		print("ok")
	elif speed>=70 and speed<=120:
		print("worning you are alert")
	else:
		print("your licence is suspend")
function()