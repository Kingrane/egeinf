f = open('ege/24file/1.txt')
s = f.readline()

m = 1
k = 1
for i in range(1, len(s)):
    if s[i] == s[i - 1]:
        k += 1
        m = max(k, m)
    else:
        k = 1
print(m)

m = 1
k = 1
for i in range(1, len(s)):
    if s[i] != s[i - 1]:
        k += 1
        m = max(k, m)
    else:
        k = 1
print(m)

# ---------------------------------

f = open('ege/24file/1.txt')
s = f.readline()
mins = []
for i in range(1, len(s) - 1):
    if ord(s[i]) < ord(s[i - 1]) and ord(s[i]) < ord(s[i + 1]):
        mins.append(i)
res = -100000
for i in range(1, len(mins)):
    if mins[i] - mins[i - 1] > res:
        res = mins[i] - mins[i - 1]
print(res)

# ---------------------------------


f = open('ege/24file/4.txt')
s = f.readline()

s1, s2 = s.split('=')

ans1 = int(s1[0])
flag = 0
for i in range(1, len(s1)):
    if s[i] == '+':
        flag = 1
    if s[i] == '-':
        flag = -1
    if s[i] in '123456789':
        ans1 += (int(s[i]) * flag)
ans2 = int(s2[0])

for i in range(len(s1) + 1, len(s2)):
    if s[i] == '+':
        flag = 1
    if s[i] == '-':
        flag = -1
    if s[i] in '123456789':
        ans2 += (int(s[i]) * flag)
print(ans2)

# ----------------------

f = open('ege/24file/5.txt')
s = f.readline()
alphavit = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
a = 0
b = [0] * 26

for i in range(1, len(s) - 1):
    if s[i - 1] == 'A' and s[i + 1] == 'R':
        for j in range(26):
            if s[i] == alphavit[j]:
                b[j] += 1
print(alphavit[b.index(max(b))])

# ----------------------

f = open('10.txt')
s = f.readline()
m = 0
k = 0  # счетчик пар подряд идущих потом умножм 2
for i in range(0, len(s), 2):
    if s[i] == s[i + 1]:
        if i >= 2:
            if s[i - 1] == s[i - 2] and s[i] == s[i - 1]:
                k = 1
            else:
                k += 1
                m = max(m, k)
    else:
        k = 0

k = 0  # Счетчик пар подряд идущих*2
for i in range(1, len(s) - 1, 2):
    if s[i] == s[i + 1]:
        if i >= 2:
            if s[i - 1] == s[i - 2] and s[i] == s[i - 1]:
                k = 1
            else:
                k += 1
                m = max(m, k)
    else:
        k = 0
print(m * 2)

# ----------------------

f = open('ege/2424/241.txt')
s = f.readline().split('X')

m = 0
for i in range(len(s) - 1):
    if (s[i].count('Y') == 1 and s[i + 1].count('Y') == 0) or \
            (s[i].count('Y') == 0 and s[i + 1].count('Y') == 1):
        m = max(len(s[i]) + len(s[i + 1]) + 1, m)

    elif s[i].count('Y') == 1 and s[i + 1].count('Y') == 1:
        m = max(len(s[i]) + 1, len(s[i + 1]) + 1, m)

    elif s[i].count('Y') > 1 and s[i + 1].count('Y') > 1:
        m = max(m, (len(s[i]) - s[i].rindex('Y') - 1) + 1 +
                (len(s[i + 1]) - s[i].index('Y') - 1))

print(m)

# ----------------------

f = open("ege/dz24/24-164.txt")
s = [i.strip() for i in f.readlines()]

k = 1
m = 0
a = []
for i in s:
    for j in range(1, len(i) - 1):
        if i[j - 1] == i[j]:
            k += 1
            m = max(k, m)
        else:
            k = 1
    k = 1
    a.append(m)
stroka = s[a.index(max(a))]
alph = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
b = []

for i in alph:
    b.append(stroka.count(i))

file = ''.join(s)
print(alph[b.index(max(b))], file.count('K'))

# ----------------------


f = open("ege/24dz/24_2023_1 (1).txt")
s = f.readline().split('A')
m = 0
k = 101
ca = 0
for i in range(1, len(s) - k + 1):
    ca = 0
    for j in range(i, i + k - 1):
        ca += len(s[j])
        if j != i + k:
            ca += 1
    m = max(m, ca)
print(m)