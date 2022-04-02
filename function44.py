def num(list):
	counter=0
	while counter<len(list):
		item=list[counter]
		if item>20:
			list.remove(item)
		else:
			counter=counter+1
			return list
		num2=[12,312,42,123,5,12,53,75,123,62,9,]
		num3=num(num2)
print("initial list",num)
print("list that doesnt contaion nunbers greate tham 20",num)
