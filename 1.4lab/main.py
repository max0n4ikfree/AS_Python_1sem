numbers = list(map(int, input("Введите числа через пробел: ").split()))

print("Исходный список:", numbers)

result = [0 if x % 2 != 0 else x for x in numbers]

print("Результат:", result)
