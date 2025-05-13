from ipaddress import ip_network, ip_address

# Заданный IP-адрес и адрес сети
ip = ip_address('119.167.50.77')
network = ip_network('119.167.48.0/255.255.255.0')

# Минимальное значение третьего байта маски
min_third_byte = 255

# Перебираем возможные значения третьего байта маски
for mask_byte in range(0, 256):
    # Создаем маску с текущим значением третьего байта
    mask = f'255.255.{mask_byte}.0'
    # Применяем маску к IP-адресу
    calculated_network = ip_network(f'{ip}/{mask}', strict=False)
    # Проверяем, совпадает ли адрес сети с заданным
    if calculated_network.network_address == network.network_address:
        if mask_byte < min_third_byte:
            min_third_byte = mask_byte

print(min_third_byte)
# ------------------------------------------
from ipaddress import *

cnt = 0
net = ip_network("231.168.192.196/255.255.255.240", 0)

for ad in net:
    if bin(int(ad))[2:].count('1') % 2 != 0:
        cnt += 1
print(cnt)
# ------------------------------------------
from ipaddress import ip_address

ip_int = int(ip_address("129.0.2.176"))
max_nodes = 0

for mask_bits in range(1, 32):
    mask = (1 << 32) - (1 << (32 - mask_bits))
    net_bits = bin(ip_int & mask).count('1')
    #host_bits = bin(ip_int & ~mask).count('1')  # Это нам больше не нужно

    if net_bits <= (32-mask_bits):
        count = 0
        for i in range(1 << (32 - mask_bits)): #перебираем все возможные номера узлов
            if bin(i).count('1') == net_bits: #если кол-во бит в номере узла == кол-ву в адресе сети
                count+=1

        max_nodes = max(max_nodes, count)

print(max_nodes)

# ------------------------------------------------------
# ----------------------ПОЛЕГЧЕ-------------------------
# ------------------------------------------------------
# ПЕРЕВОД ИЗ 10 В 2 АЙПИ ВЕСЬ

ip = input()
a = []

for i in ip.split('.'):
    binip = bin(int(i))[2:].zfill(8)
    a.append(binip)

print('.'.join(a))

# ------------------ решение какой-то части / перебор возможных
from itertools import *

cnt = 0
sp = []
for a in product('01', repeat=8):
    s = ''.join(a)
    if 8 > 5 + s.count('1'):
        sp.append(int(s, 2))
print(max(sp))
# ------------------ ПЕРЕВОД ИЗ 2 В 10

print(int('11111110', 2))


