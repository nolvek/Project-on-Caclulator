a = int(input())
b = int(input())
if b != 10 or 2 < b < 16:
        a = int(str(a), b)
else:
    s1 = str(a)[::-1]
    for i in range(len(s1)):
        s0 += int(s1[i]) * b**i
    a = s0
print(a)
