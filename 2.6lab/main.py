if __name__ == "__main__":
    pass
def modulus(z):
    return (z.real**2 + z.imag**2)**0.5

def multiply(z1, z2):
    return z1 * z2

def divide(z1, z2):
    return z1 / z2
    import cmath

# Пример использования
z1 = complex(3, 4)
z2 = complex(1, 2)

print(modulus(z1))        # 5.0
print(multiply(z1, z2))   # (-5+10j)
print(divide(z1, z2))     # (2.2-0.4j)
