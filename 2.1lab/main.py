print("а) Введите числа через пробел:")
chisla = input().split()
summa = 0
for x in chisla:
    summa += int(x)
print("Сумма:", summa)

# б) Список в словарь
print("\nб) Введите слова через пробел:")
slova = input().split()
slovar = {}
for x in slova:
    slovar[x] = {}
print("Словарь:", slovar)

# в) Проверка одинаковых значений
print("\nв) Введите числа через пробел:")
chisla2 = input().split()
odinakovie = True
pervoe = chisla2[0]
for x in chisla2:
    if x != pervoe:
        odinakovie = False
        break
print("Все одинаковые:", odinakovie)
