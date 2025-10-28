price_per_kg = float(input("Введите цену за 1 кг конфет: "))

print("Вес (кг) | Стоимость")
print("---------|-----------")
for weight in [1.2, 1.4, 1.6, 1.8, 2.0]:
    cost = price_per_kg * weight
    print(f"{weight:6.1f}  | {cost:8.2f}")
