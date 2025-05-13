import itertools
count = 0
for x in itertools.product('ЛАГЕРЬ', repeat=6):
  # ПРОВЕРКА НА УНИКАЛЬНОСТЬ БУКВ И ОТСУТСТВИИ "Ь"
  if x.count('Л') == 1 and x.count('А') == 1 and x.count('Г') == 1 and x.count('Е') == 1 and x.count('Р') == 1 and x.count('Ь') == 1 and x[0] != 'Ь':
  # ПРОВЕРКА НА ЕА
    for i in range(len(x)):
      if x[i-1] != 'Е' and x[i] != 'А':
        count += 1
        print(count, ''.join(x))
################
from itertools import product

count = 0
for x in product(''.join(sorted(list("МАНГУСТ"))), repeat=6):
    count += 1
    if x[0] != 'А' and x.count('М') == 2 and x.count('У') <= 1:
        print(count)
        break

################
import itertools
count = 0
for x in itertools.product('КУРИЦА', repeat=4):
  # ПРОВЕРКА НА "У" ХОТЯ БЫ 2 РАЗ
  if x.count('У') >= 2:
    count += 1
    print(count, ''.join(x))
################
import itertools
count = 0
for x in itertools.product('СЛОН', repeat=4):
  # ПРОВЕРКА НА УНИКАЛЬНОСТЬ БУКВ И ОТСУТСТВИИ В НАЧАЛЕ "Н"
  if x.count('С') == 1 and x.count('Л') == 1 and x.count('О') == 1 and x.count('Н') == 1 and x[0] != 'Н':
    count += 1
    print(count, ''.join(x))

              
# ЕГЭ
a = 'АПРСУ'
count = 0
for a1 in a:
    for a2 in a:
        for a3 in a:
            for a4 in a:
                for a5 in a:
                    x = a1+a2+a3+a4+a5
                    count += 1
                  
                    if a1 == 'У' and 'АА' not in x:
                      print(count, x)
                      break
            
a = 'ИЕАУОЯ'
k = 0
for a1 in a:
    for a2 in a:
        for a3 in a:
            for a4 in a:
                for a5 in a:
                    b = a1+a2+a3+a4+a5
                    if a5 == 'Е': # оканчивается на "Е"
                        if a1 != a3 and a2 != a4 and a3 != a5: # не совпадают буквы идущие через одну
                          if 'А' in b:
                            k += 1
                            print(k, b)

from itertools import product

k = 0
for x in product("01234567", repeat=5):
    s = ''.join(x)
    if s[0] != '0' and s.count('6') == 1:
        if "61" not in s and "63" not in s and "65" not in s and \
                "67" not in s and "16" not in s and "36" not in s and \
                "56" not in s and "76" not in s:
            k += 1
print(k)



from itertools import product

cnt = 0

for length in range(1, 7):
    for x in product("ABCDEFGHIJKLMNOPQRSTUVWXYZ", repeat=length):
        s = "".join(x)
        cnt += 1
        if s == "FEDABC":
            print(cnt)
            break
