# 19-21 2 куча
from functools import lru_cache


def moves(h):  # h-это 2 кучи сразу (кортеж)
    a, b = h  # а-первая куча , b-вторая
    return (a + 2, b), (a + 3, b), (a * 2, b), (a, b + 2), (a, b + 3), (a, b * 2)


@lru_cache(None)
def f(h):
    if sum(h) >= 51:
        return 'End'
    if any(f(x) == 'End' for x in moves(h)):
        return 'Win1'
    if all(f(x) == 'Win1' for x in moves(h)):
        return 'Lose1'
    if any(f(x) == 'Lose1' for x in moves(h)):
        return 'Win2'
    if all(f(x) == 'Win2' for x in moves(h)):
        return 'Lose2'


# Поиск неудачного хода
for s in range(1, 46):
    h = (5, s)
    if any(f(x) == 'Win1' for x in moves(h)):
        print(h, 'Axxa Петя неудачник')

# ----------------
# 19
from functools import lru_cache


def moves(h):
    a, b = h
    return (a + 1, b), (a * 2, b), (a, b + 1), (a, b * 2)


@lru_cache(None)
def f(h):
    if sum(h) >= 86:
        return 'End'
    if any(f(x) == 'End' for x in moves(h)):
        return 'Win1'
    if all(f(x) == 'Win1' for x in moves(h)):
        return 'Lose1'
    if any(f(x) == 'Lose1' for x in moves(h)):
        return 'Win2'
    if all(f(x) == 'Win2' or f(x) == 'Win1' for x in moves(h)):
        return 'Lose12'


for s in range(1, 72):
    h = (14, s)
    if f(h) == 'Lose12':
        print(h, f(h))