def modulus(z):
    return (z.real**2 + z.imag**2)**0.5

def multiply(z1, z2):
    return z1 * z2

def divide(z1, z2):
    return z1 / z2
    import cmath

z1 = complex(3, 4)
z2 = complex(1, 2)

print(modulus(z1))
print(multiply(z1, z2))
print(divide(z1, z2))
