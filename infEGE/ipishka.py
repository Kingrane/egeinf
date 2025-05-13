ip = input()
a = []

for i in ip.split('.'):
    binip = bin(int(i))[2:].zfill(8)
    a.append(binip)

print('.'.join(a))

# ------------------
from itertools import *

cnt = 0
sp = []
for a in product('01', repeat=8):
    s = ''.join(a)
    if 8 > 5 + s.count('1'):
        sp.append(int(s, 2))
print(max(sp))
# ------------------

print(int('11111110', 2))

