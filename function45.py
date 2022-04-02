def function():
	a=["sai,priya","neetu,kumari","rani,rajput"]
	i=0
	l=[]
	while i<len(a):
	       if "," in a[i]:
               s=a[i].replace(",","")
               l.append(s)
               
            i+=1
	print(l)
function()