if __name__ == "__main__":
    pass
def Quarter(x, y):
    """
    Определяет номер координатной четверти для точки (x, y)
    x, y - вещественные координаты (ненулевые)
    Возвращает: 1, 2, 3 или 4
    """
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4

# Примеры использования
print(Quarter(2.5, 3.1))   # 1
print(Quarter(-1.8, 4.2))  # 2
print(Quarter(-3.5, -2.1)) # 3
print(Quarter(4.7, -1.9))  # 4
