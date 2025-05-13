
f = open("ege/17file/6 17.txt")

n = 100000
a = [int(i) for i in f.readlines()]
m11 = min([x for x in a if x % 11 == 0])
res = []

for i in range(len(a) - 1):
    x, y = a[i], a[i + 1]
    if x > m11 and y > m11:
        if '21' in str(x) or '12' in str(x) or '21' in str(y) or '12' in str(y):
            res.append(x*y)
print(len(res), max(res))
# ------------------------

f = open('ege/17file/7 17.txt')

a = [int(i) for i in f.readlines()]
max127 = max([i for i in a if i % 127 == 0])
res = []

for i in range(len(a) - 1):
    x, y = a[i], a[i + 1]
    if '31' in str(oct(x)[2:]) or '31' in str(oct(y)[2:]):
        if x > max127 or y > max127:
            res.append(x+y)

print(len(res), min(res))

# ------------------------

def five(x):
    s = ''
    while x > 0:
        s = str(x % 5) + s
        x //= 5
    return s


f = open("ege/17file/9 dz17-30.txt")

a = [int(i) for i in f.readlines()]
b = [x for x in a if x % 31 == 0]
sr = sum(b) / len(b)
k = 0
mi = 10000000000

for i in range(len(a) - 2):
    x, y, z = a[i], a[i + 1], a[i + 2]
    p = five(sum([int(i) for i in str(x) + str(y) + str(z)]))
    if p == p[::-1]:
        if (x + y + z) / 3 > sr:
            k += 1
            mi = min(mi, x + y + z)
print(k, mi)
# ------------------------


def sem(x):
    s = ''
    while x > 0:
        s = str(x % 7) + s
        x //= 7
    return s


f = open('ege/17file/17_2024_2 (2).txt')
a = [int(i) for i in f.readlines()]
min3 = min([x for x in a if sem(x)[-1] == '3'])

res = []
for i in range(len(a) - 1):
    x, y = a[i], a[i + 1]
    if x > min3 and y > min3:
        res.append(x ** 2 + y ** 2)

print(len(res), max(res))

# ------------------------


f = open('ege/17file/12 5.txt')
n = int(f.readline())
a = [int(i) for i in f.readlines()]

res = []
for i in range(n):
    for j in range(i + 3, n):
        x, y = a[i], a[j]
        if (x * y) % 26 == 0:
            res.append(x + y)

print(len(res))



