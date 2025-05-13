'''a'''
'''1=34

f = open("ege/24dz/24_2 (1).txt")
s = f.readline()

k = 0
m = 0
for i in range(len(s)):
    if s[i] != 'Z':
        k += 1
        m = max(m, k)
    else:
        k = 0
print(m)'''

'''2=119
f = open("ege/24dz/24_3 (1).txt")
s = f.readline()

k = 1
m = 0
for i in range(1, len(s) - 1):
    if s[i - 1] != s[i]:
        k += 1
        m = max(m, k)
    else:
        k = 1
print(m)'''

'''3=20
f = open("ege/24dz/24_4.txt")
s = f.readline()

k = 1
m = 0
for i in range(1, len(s) - 1):
    if (not ((s[i - 1] + s[i]).isdigit())) and \
            not (s[i - 1] + s[i] in 'ABBABCCBACCAA'):
       k += 1
       m = max(k, m)
    else:
        k = 1
print(m)'''

'''4=7684
f = open("ege/24dz/24_6.txt")
s = f.readline()
s = s.replace('000', 'A')

k = 0
m = 0

for i in range(len(s) - 1):
    if s[i] != 'A':
        k += 1
        m = max(m, k)
    else:
        k = 0
print(m + 4)'''

'''5=50

f = open("ege/24dz/24_7 (1).txt")
s = f.readline()
k = 0
m = 0
z = 0

for i in range(len(s) - 1):
    if s[i] == 'Z':
        z += 1
        if z != 3:
            k += 1
        if z == 3:
            m = max(m, k)
            k = 0
            z = 0
    else:
        k += 1

print(m + 4)'''

'''6=19
f = open("ege/24dz/24_9.txt")
s = f.readline()

k = 0
m = 0
a = 0

for i in range(len(s) - 1):
    if a > len(s) - 1:
        break
    else:
        if s[a] == 'A' and (s[a + 1] == 'B' or s[a + 1] == 'C'):
            k += 1
            m = max(m, k)
            a += 2
        else:
            k = 0
            a += 1
print(m)'''

'''7=
f = open("ege/24dz/24_du_1.txt")
s = f.readline()

k = 0
m = 10000000
f = 0
for i in range(len(s) - 1):
    if s[i] == 'F':
        f += 1
        if f != 2025:
            k += 1
        if f == 2025:
            m = min(m, k)
            k = 0
            f = 0
    else:
        k += 1

print(m)'''
# 1
'''f=open('24_du_1 (1).txt')
s = f.read().strip()
l=r=count=0
kmin=10**10
for r in range(len(s)):
    if s[r]=='F': count += 1
    while count == 2025:
        kmin = min(kmin, r-l+1)
        if s[l]=='F': count -= 1
        l += 1

print(kmin)'''
'''
f = open('24_du_.txt')
s = f.read().strip()
# s='FBBFBBBFBBFBFB'
# a=s.split('F')
# t=3
t = 300
a = s.split('F')
m = 10 * 100
for i in range(0, len(a) - t):
    st = ''
    for j in range(i, i + t + 1):
        st += a[j]
        if j != i + t:
            st = st + 'F'
    m = min(m, len(st))
print(m)'''

'''
f = open("ege/24dz/24_2024_07.txt")
s = f.readline().strip()

s = s.replace('-', '*').split('*')

k = 0
m = 0
sp = []
a = ''
for i in range(len(s)):
    if s[i] != '' and s[i][0] != '0':
        a = a + '*' + s[i]
    else:
        sp.append(a)
        m = max(m, len(a))
        a = ''
print(sp)
print(m - 1)'''

f = open("ege/24dz/24_2024_3.txt")
s = f.readline().strip()
sp = []
maxa = 0
s = s.replace('++', '?')
s = s.replace('*+', '?')
s = s.replace('**', '?')
s = s.replace('+*', '?')
s = s.split('?')
for i in range(len(s)):
    p = s[i].strip('+*')
    p = p.split('+')
    flag = True

    for j in range(len(p)):
        cifri = p[j].split('*')
        for c in cifri:
            if len(c) > 1 and c[0] == '0':
                flag = False
                break
        if flag is False:
            break
        if '0' in p[j]:
            flag = True
        else:
            flag = False
            break

    if flag is True:
        a = '+'.join(p)
        if len(a) > 121:
            sp.append((a, len(a)))
        maxa = max(maxa, len(a))

for i in sp:
    print(i)
print(maxa)
