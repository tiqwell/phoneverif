st = [0, 1, 2, 3, 4]
a = st[0]
b = st[1]
c = st[2]
d = st[3]
e = st[4]

a = a + b
a //= c
c += b
b += d
e -= a
b = a + b + c
d = c + d + b
b += 1072
d += 1067

print(chr(d), end="")
print(chr(b), end="")
