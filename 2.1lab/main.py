if __name__ == "__main__":
    pass
def sum_dict_values(dictionary):
    
    return sum(dictionary.values())

def list_to_nested_dict(lst):
   
    return {item: {} for item in lst}

def all_values_equal(dictionary):

    if not dictionary:  
        return True
    values = list(dictionary.values())
    return all(value == values[0] for value in values)

if __name__ == "__main__":
    print("а) Сумма значений словаря:")
    dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
    result1 = sum_dict_values(dict1)
    print(f"{dict1} → {result1}")
    
    print("\nб) Преобразование списка в словарь:")
    list1 = ['a', 'b', 'c']
    result2 = list_to_nested_dict(list1)
    print(f"{list1} → {result2}")
    
    print("\nв) Проверка одинаковости значений:")
    dict2 = {'a': 1, 'b': 1, 'c': 1}
    dict3 = {'a': 1, 'b': 2, 'c': 1}
    result3 = all_values_equal(dict2)
    result4 = all_values_equal(dict3)
    print(f"{dict2} → {result3}")
    print(f"{dict3} → {result4}")
    
    print("\nДополнительные примеры:")
    
    empty_dict = {}
    print(f"Пустой словарь {empty_dict} → {all_values_equal(empty_dict)}")
    
    list2 = ['x', 'y', 'z']
    print(f"Список {list2} → {list_to_nested_dict(list2)}")
    
    mixed_dict = {'a': 5, 'b': 5.0, 'c': 5}
    print(f"Смешанный словарь {mixed_dict} → {all_values_equal(mixed_dict)}")
