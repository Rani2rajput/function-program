def fun(*l):
	i=0
	while i<len(l):
        j=0
        while j<len(l):
            k=0
            while k<len(l):
                print(l[i]+l[j]+l[k])
                k+=1
            j+=1
        i+=1
fun("2","3","4")