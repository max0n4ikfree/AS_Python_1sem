n = int(input("Введите натуральное число n: "))

total_sum = 0
factorial = 1

for i in range(1, n + 1):
    factorial *= i
    total_sum += 1 / factorial

# Вывод результата
print(f"Сумма ряда: {total_sum:.10f}")
