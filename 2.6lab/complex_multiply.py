def multiply(z1, z2):
    real = z1[0]*z2[0] - z1[1]*z2[1]
    imag = z1[0]*z2[1] + z1[1]*z2[0]
    return (real, imag)