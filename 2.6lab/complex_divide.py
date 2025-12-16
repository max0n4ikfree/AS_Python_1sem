def divide(z1, z2):
    denom = z2[0]**2 + z2[1]**2
    real = (z1[0]*z2[0] + z1[1]*z2[1]) / denom
    imag = (z1[1]*z2[0] - z1[0]*z2[1]) / denom
    return (real, imag)