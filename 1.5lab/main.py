numbers = list(map(int, input("Введите числа через пробел: ").split()))

print("Исходный список:", numbers)

result = sorted([x for x in numbers if x % 3 == 0])

print("Числа, кратные 3, упорядоченные по возрастанию:", result)
