if __name__ == "__main__":
    pass
def filter_and_sort_2(lst):
    """
    Выбирает числа кратные 3 и сортирует по возрастанию.
    Использует функцию filter().
    """
    multiples_of_3 = filter(lambda x: isinstance(x, int) and x % 3 == 0, lst)
    return sorted(multiples_of_3)
