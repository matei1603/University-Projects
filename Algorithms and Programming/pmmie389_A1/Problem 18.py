x=int(input("first number: "))
y=int(input("second number: "))
v=[0]*10
v1=[0]*10
aux=0
while x>0:
    v[x%10] = 1
    x=x//10

while y>0:
   v1[y%10]=1
   y=y//10
i=1
while i<10:
    if v[i]==1 and v1[i]==1:
        aux=aux+1
    i=i+1
print(aux)
i=1
while i<10:
    if v[i]==1 and v1[i]==1:
        print(i)
    i=i+1
