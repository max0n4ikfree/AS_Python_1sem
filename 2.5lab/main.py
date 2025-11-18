if __name__ == "__main__":
    pass
def bin_sum(a, b):
    """Сложение двоичных чисел"""
    return bin(int(a, 2) + int(b, 2))


positive_bin = "1101"
negative_bin = "-101"

result = bin_sum(positive_bin, negative_bin)
print(f"{positive_bin} + ({negative_bin}) = {result}")  # 1101 + (-101) = 0b1000
