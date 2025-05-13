f = open('24_2024_3.txt')
s = f.read().strip()


# Функция проверяет ариф. выр. на ноль
# В выражении может быть только *
def F(s):
    if s != '' and ((s.find('*') != -1 and (s.find('*0*') != -1 or s[:2] == '0*' or s[-2:] == '*0')) or (s == '0')):
        return True
    else:
        return False


s = s.replace('+*', '$').replace('**', '$').replace('++', '$').replace('*+', '$')
kmax = 0
a = s.split('$')
for i in range(len(a)):
    b = a[i].strip('*+').split('+')
    st = ''
    for j in range(len(b)):
        if F(b[j]):
            # Формируем цепочку-кандидата
            if st != '':
                st = st + '+' + b[j]
            else:
                st = st + b[j]
            kmax = max(kmax, len(st))
        else:
            # К новой цепочке пытаемся добавить начало
            st = ''
            for k in range(1, len(b[j]) + 1):
                if F(b[j][-k:]):
                    st = b[j][-k:]

            kmax = max(kmax, len(st))

print(kmax)
