def binary_add(a, b):
    # Делаем числа одинаковой длины
    n = max(len(a), len(b))
    a = a.zfill(n)
    b = b.zfill(n)
    
    result = ""
    carry = 0
    
    # Складываем справа налево
    for i in range(n-1, -1, -1):
        total = int(a[i]) + int(b[i]) + carry
        result = str(total % 2) + result
        carry = total // 2
    
    if carry:
        result = "1" + result
    
    return result

# Ввод чисел
num1 = input("Первое двоичное число: ")
num2 = input("Второе двоичное число: ")

# Вычисление суммы
sum_result = binary_add(num1, num2)
print(f"Сумма: {sum_result}")
