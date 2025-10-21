if __name__ == "__main__":
    pass
price = float(input("Введите цену за 1 кг: "))
print("Способ 1:")
current_weight = 1.2
while current_weight <= 2.01:
    cost = price * current_weight
    print(f"{current_weight} кг: {cost:.2f} руб.")
    current_weight += 0.2
