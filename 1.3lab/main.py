if __name__ == "__main__":
    pass
n = int(input("Введите натуральное число n: "))
sum1 = 0
for i in range(1, n + 1):
    factorial = 1
    for j in range(1, i + 1):
        factorial *= j
    sum1 += 1 / factorial

print(f"Способ 1: Сумма = {sum1:.10f}")
