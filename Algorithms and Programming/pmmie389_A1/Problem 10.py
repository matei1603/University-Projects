def numbers_of_(a):
    nr = 0
    while a > 0:
        if a % 10 == 5:
            nr = nr + 1
        a = a // 10
    return nr


v = []
p = 0
while True:
    x = int(input("Numbers: "))
    if x == 0:
        break
    v.append(x)

for i in range(0, len(v)-1):
    if numbers_of_(v[i]) > numbers_of_(v[i + 1]):
        p = p + 1

print(p)
