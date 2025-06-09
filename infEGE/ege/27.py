# вот

A = [[], []]
B = [[], [], []]

for line in open("ege/27files/27-51a.txt"):
    x, y = [float(i) for i in line.replace(',', '.').split()]
    if x < 4:
        A[0].append([x, y])
    elif x > 7:
        A[1].append([x, y])

for line in open("ege/27files/27-51b.txt"):
    x, y = [float(i) for i in line.replace(',', '.').split()]
    if (8.8 > x > 3) and (y <= 7.5):
        B[0].append([x, y])
    elif (y >= 8.2) and (14 > x > 5):
        B[1].append([x, y])
    elif (14.8 >= x > 10) and (y < 6):
        B[2].append([x, y])


def d(a, b):
    x1, y1 = a
    x2, y2 = b
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def centers(cl):
    m = []
    for p in cl:
        sm = sum(d(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]


centerA = [centers(cl) for cl in A]
centerB = [centers(cl) for cl in B]
pxa = int(sum(x for x, y in centerA) / 2 * 100000)
pya = int(sum(y for x, y in centerA) / 2 * 100000)
pxb = int(sum(x for x, y in centerB) / 3 * 100000)
pyb = int(sum(y for x, y in centerB) / 3 * 100000)
print(pxa, pya)
print(pxb, pyb)
# -------------------------------------------------------
# -------------------------------------------------------
# -------------------------------------------------------
A = [[], []]
B = [[], [], []]

for line in open("A.txt"):
    x, y = [float(i) for i in line.split()]
    if y < 3:
        A[0].append([x, y])
    else:
        A[1].append([x, y])

for line in open("B.txt"):
    x, y = [float(i) for i in line.split()]
    if y < -x + 8:
        B[0].append([x, y])
    elif y > 1.5 * x - 6.5:
        B[1].append([x, y])
    else:
        B[2].append([x, y])


def d(a, b):
    x1, y1 = a
    x2, y2 = b
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def center(cl):
    m = []
    for p in cl:
        sm = sum(d(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]


centerA = [center(cl) for cl in A]
centerB = [center(cl) for cl in B]
pxa = int(sum(x for x, y in centerA) / 2 * 100000)
pya = int(sum(y for x, y in centerA) / 2 * 100000)
pxb = int(sum(x for x, y in centerA) / 3 * 100000)
pyb = int(sum(y for x, y in centerA) / 3 * 100000)
print(pxa, pya)
print(pxb, pyb)

# -------------------------------------------------------
# -------------------------------------------------------
# ----------------------+высота--------------------------

A = [[], []]
B = [[], [], []]

for line in open("ege/27files/27-26a.txt"):
    x, y, h = [float(i) for i in line.replace(',', '.').split()]
    if x < 200:
        A[0].append([x, y, h])
    if x > 300:
        A[1].append([x, y, h])

for line in open("ege/27files/27-26b.txt"):
    x, y, h = [float(i) for i in line.replace(',', '.').split()]
    if (x < -50) and (y < -50):
        B[0].append([x, y, h])
    if (x < 0) and (x > -100) and (y > 0):
        B[1].append([x, y, h])
    if (x > 100) and (x < 200) and (y > -100):
        B[2].append([x, y, h])


def d(a, b):
    x1, y1 = a[0], a[1]
    x2, y2 = b[0], b[1]
    return ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5


def center(cl):
    m = []
    for p in cl:
        sm = sum(d(p, p1) * p1[2] for p1 in cl)
        m.append([sm, p])
    return min(m)[1]


cA = [center(cl) for cl in A]
cB = [center(cl) for cl in B]
pxa = int(sum(p[0] for p in cA) / 2 * 100000)
pya = int(sum(p[1] for p in cA) / 2 * 100000)
pxb = int(sum(p[0] for p in cB) / 3 * 100000)
pyb = int(sum(p[1] for p in cB) / 3 * 100000)
print(pxa, pya)
print(pxb, pyb)

# -------------------------------------------------------
# -------------------------------------------------------
# -------------------------------------------------------

data = []
for line in open("ege/27files/27_A_21931.txt"):
    x, y = [float(i) for i in line.replace(',', '.').split()]
    data.append([x, y])


def d(a, b):
    x1, y1 = a
    x2, y2 = b
    return ((x2 - x1) ** 2 + (y2 - y1) ** 2) ** 0.5


def center(cl):
    m = []
    for p in cl:
        sm = sum(d(p, p1) for p1 in cl)
        m.append([sm, p])
    return min(m)[1]


clusters = []
while data:
    cl = [data.pop()]
    for p in cl:
        sosed = [p1 for p1 in data if d(p, p1) < 1]
        for p1 in sosed:
            cl.append(p1)
            data.remove(p1)
    clusters.append(cl)

print([len(cl) for cl in clusters])

c = [center(cl) for cl in clusters]
px = int(sum(x for x, y in c) / len(c) * 10000)
py = int(sum(y for x, y in c) / len(c) * 10000)
print(px, py)
