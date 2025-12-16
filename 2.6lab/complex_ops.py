def modulus(z):
    return (z[0]**2 + z[1]**2)**0.5

def multiply(z1, z2):
    real = z1[0]*z2[0] - z1[1]*z2[1]
    imag = z1[0]*z2[1] + z1[1]*z2[0]
    return (real, imag)

def divide(z1, z2):
    denom = z2[0]**2 + z2[1]**2
    real = (z1[0]*z2[0] + z1[1]*z2[1]) / denom
    imag = (z1[1]*z2[0] - z1[0]*z2[1]) / denom
    return (real, imag)