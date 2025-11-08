# Для задач на простые делители или & без доп условий.
from xml.etree.ElementTree import QName

pass # Вар 1
# + просто, понятно.
for a in range(1, 1000):
    flag = 1
    for x in range(1, 10000):
        if(...):
            ...
        # или! ЧТО БУДЕТ ЛУЧШЕ
        f = ...
        if f == 0:
            flag =0
            break
    if(flag == 1):
        print(a)

pass # Вар 2
# + оптимально и так же понятно
# - новая версия питона как я помню...
for a in range(1, 1000):
    for x in range(1, 1000):
        f = ...
        if f == 0:
            break
    else:
        print(a)

pass # Вар 3 САМЫЙ УНИВЕРСАЛЬНЫЙ.
# + универсален и для дальнейших задачек.
# - надо понимать область определения переменных.
def f(x):
    return ...
for a in range(1, 1000):
    if all(f(x) == 1 for x in range(1000)):
        print(a)

# Для задач на множества
pass # Вар 1 / 1.1 На списки с условием
# a = set() // для минимального массива.
a = set(x for x in range(1000)) # для макс массива.

def f(x):
    A = x in a
    B = x in {}
    C = x in {}
    return ...
for x in range(1000):
    if f(x) == 0:
        # a.add(x) // для минимального массива.
        a.remove(x) # для макс массива.
print(a)

pass # Вар 2 На список с генерацией. (тут пример макс массива)
from itertools import *
bit = [''.join(i) for i in product('01', repeat=8)]

a = set()
p = {i for i in bit if ...}
q = {i for i in bit if ...}

def f(x):
    A = x in a
    P = x in p
    Q = x in q
    return ...

for x in bit:
    if f(x) == 0:
        a.add(x)
print(len(a))

pass # Вар 3 На отрезки.
from itertools import *

def f(x):
    A = 32442<= x <=2321
    P = 32442<= x <=2321
    Q = 32442<= x <=2321
    return ...

Ox = [i/4 for i in range(24*4, 51*4+1)] # Брать число мин в условии -1 и макс число из условия + 1
m = []

for a1, a2 in combinations(Ox, 2):
    if all(f(x) == 0 for x in Ox):
        m.append(a2-a1)
print(max(m))