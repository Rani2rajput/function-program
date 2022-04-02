def fun():
	list=[2,-7,5,-64,-14]
	i=0
	count=0
	count1=0
	while i<len(list):
		if list[i]>0:
			count+=1
		elif list[i]<0:
			count1+=1
		i+=1
	print("negative numbers: ",count)
	print("positive numbers: ",count1)
fun()