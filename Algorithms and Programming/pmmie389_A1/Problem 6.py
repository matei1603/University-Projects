d1=int(input("d1="))
m1=int(input("m1="))
y1=int(input("y1="))
d2=int(input("d2="))
m2=int(input("m2="))
y2=int(input("y2="))
v=y1-y2
if m1<m2:
    v=v-1
elif m1==m2:
    if d1<d2:
		v=v-1
print(v)
