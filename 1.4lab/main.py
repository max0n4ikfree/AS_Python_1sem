if __name__ == "__main__":
    pass
def zero_odd_numbers_3(lst):
    """
    Обнуляет все нечетные числа в списке.
    Изменяет исходный список.
    """
    for index, value in enumerate(lst):
        if isinstance(value, int) and value % 2 != 0:
            lst[index] = 0
    return lst
