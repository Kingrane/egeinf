from functools import lru_cache


def moves(h):
    return h + 1, h * 2


@lru_cache(None)
def f(h):
    if h >= 92:
        return 'End'
    if any(f(x) == 'End' for x in moves(h)):
        return 'Win1'
    if all(f(x) == 'Win1' for x in moves(h)):
        return 'Lose1'
    if any(f(x) == 'Lose1' for x in moves(h)):
        return 'Win2'
    if all(f(x) == 'Win2' or f(x) == 'Win1' for x in moves(h)):
        return 'Lose12'


for i in range(1, 92):
    if f(i) == 'Lose1':
        print(i)

# -------------------------------------------
from functools import lru_cache


def moves(h):
    return [h + k for k in range(1, h + 1) if h % k == 0]


@lru_cache(None)
def f(h):
    if h >= 92:
        return 'End'
    if any(f(x) == 'End' for x in moves(h)):
        return 'Win1'
    if all(f(x) == 'Win1' for x in moves(h)):
        return 'Lose1'
    if any(f(x) == 'Lose1' for x in moves(h)):
        return 'Win2'
    if all(f(x) == 'Win2' or f(x) == 'Win1' for x in moves(h)):
        return 'Lose12'


for i in range(1, 92):
    if f(i) == 'Lose1':
        print(i)