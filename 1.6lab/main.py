if __name__ == "__main__":
    pass
def reverse_strings_if_multiple_of_four(string_list):
    """
    Переворачивает строки в списке, если их длина кратна 4
    """
    result = []
    for s in string_list:
        if len(s) % 4 == 0:
            result.append(s[::-1])
        else:
            result.append(s)
    return result
strings = ["abcd", "hello", "test", "12345678", "python", "word"]
reversed_strings = reverse_strings_if_multiple_of_four(strings)
for original, reversed_str in zip(strings, reversed_strings):
    print(f"'{original}' (длина: {len(original)}) -> '{reversed_str}'")
