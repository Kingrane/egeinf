# У исполнителя Калькулятор две команды, которым 

# Содержит
def make(x, y):
    if x == y:
        return 1
    elif x > y:
        return 0
    elif x < y:
        return make(x + 1, y) + make(x + 2, y)


n = make(5, 10) * make(10, 15)
print(n)


# Содержит 16 | Не содержит 56
def f(x, y):
    if x == y:
        return 1
    elif x > y or x == 45:
        return 0
    elif x < y:
        return f(x + 1, y) + f(x * 3, y)


n = f(3, 16) * f(16, 52)
print(n)


# --------------------------------
def f(a, b, s=''):
    if a == b:
        return 1 if s.count('3') + s.count('4') == 1 else 0
    if a > b:
        return 0
    if a < b:
        return f(a + 1, b, s + '1') + f(a + 2, b, s + '2') + \
            f(a * 2, b, s + '3') + f(a * 3, b, s + '4')


print(f(1, 11, ''))
# --------------------------------

def f(a, b):
    if a == b:
        return 1
    if a > b:
        return 0
    if a < b:
        return f(a + 1, b) + f(a + 3, b) + f(a + a - 1, b)


print(f(2, 10))

# --------------------------------
def f(a, b, s=''):
    if a == b:
        if '33' not in s and '44' not in s and \
                '34' not in s and '43' not in s and \
                '11' not in s and '22' not in s and \
                '12' not in s and '21' not in s:
            return 1
        return 0
    if a > b:
        return 0
    if a < b:
        return f(a + 1, b, s + '1') + f(a + 2, b, s + '2') + \
            f(a * 2, b, s + '3') + f(a * 3, b, s + '4')


print(f(1, 24, ''))
