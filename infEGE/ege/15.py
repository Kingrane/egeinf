def treug(n, m, k):
    a = sorted([n, m, k])
    return a[2] < a[1] + a[0]


def f(x, A):
    return not ((treug(x, 11, 16) == (not (max(x, 5) > 10))) and treug(4, A, x))


for A in range(1000, 1, -1):
    if all(f(x, A) == 1 for x in range(1, 1000)):
        print(A)
        break

# --------------------------
def f(m, n):
    return ((3 * m + 4 * n) > 66) or (m <= A) or (n < A)


for A in range(1000):
    if all(f(m, n) == 1 for m in range(1000) for n in range(1000)):
        print(A)
        break

# --------------------------

for A in range(100):
    if all((x & 25 != 0) <= ((x & 17 == 0) <= (x & A != 0)) for x in range(100)):
        print(A)
        break
# --------------------------

def f(x):
    return ((x & 21074) != 0) <= (((x & 12369) == 0) <= ((x & A) != 0))


for A in range(1000000):
    if all(f(x) == 1 for x in range(1000000)):
        print(A)
        break

# --------------------------
def Del(n, m):
    return n % m == 0


B = [int(x) for x in range(132, 151)]

for A in range(2, 1000):
    valid = True
    for x in range(1, 1000):
        if not ((not Del(x, A) and x in B) <= (not Del(x, 13))):
            valid = False
            break
    if valid:
        print(A)
        break

# -------------------------- otrezki
m = 0
P = range(5, 31)
Q = range(14, 24)
for start in range(1, 50):
    for end in range(start + 1, 51):
        A = range(start, end)
        if all(((x in P) == (x in Q)) <= (x not in A) for x in range(1000)):
            m = max(m, end - start)
print(m)
# --------------------------

for A in range(100):
    if all(((4 * x + 3 * y) < A) or (x >= y) or (y >= 13) for x in range(100) for y in range(100)):
        print(A)
        break
# -------------------------- del

for A in range(1000, 1, -1):
    if all((x % A != 0) <= ((x % 6 == 0) <= (x % 4 != 0)) for x in range(100)):
        print(A)
        break

