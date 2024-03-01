y = int(input("Year: "))
d = int(input("Days: "))
v = [31,28,31,30,31,30,31,31,30,31,30,31]
if (y % 4 == 0 and (y % 100 != 0 or y % 400 == 0)):
    v[1] = v[1]+1
i=0
m=1
while d>v[i]:
    m+=1
    d=d-v[i]
    i+=1
print(d,m,y)


