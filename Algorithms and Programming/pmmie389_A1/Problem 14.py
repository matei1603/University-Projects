n=int(input("n="))
aux=0
while n:
	ifn%2==0:
		n=n//2
	else:
		aux=aux+1
		n=n//2
print(aux," ")