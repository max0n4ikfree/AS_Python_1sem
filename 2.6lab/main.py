import complex_ops

z1 = (3, 4)
z2 = (1, 2)

print("z1 =", z1)
print("z2 =", z2)
print("Модуль z1:", complex_ops.modulus(z1))
print("Умножение:", complex_ops.multiply(z1, z2))
print("Деление:", complex_ops.divide(z1, z2))