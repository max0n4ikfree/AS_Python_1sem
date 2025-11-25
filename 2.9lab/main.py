if __name__ == "__main__":
    pass
import pickle

def read_matrices(filename):
    with open(filename, 'rb') as f:
        return pickle.load(f)

def write_matrices(filename, data):
    with open(filename, 'wb') as f:
        pickle.dump(data, f)

def multiply_matrices(A, B):
    return [[sum(a * b for a, b in zip(row, col)) for col in zip(*B)] for row in A]


m1 = read_matrices('file1.dat')
m2 = read_matrices('file2.dat')


result = [(A, B, multiply_matrices(A, B)) for A, B in zip(m1, m2)]


write_matrices('file3.dat', result)


print("Файл 1:")
for i, mat in enumerate(m1):
    print(f"Матрица {i+1}: {mat}")

print("\nФайл 2:")
for i, mat in enumerate(m2):
    print(f"Матрица {i+1}: {mat}")

print("\nФайл 3:")
for i, (A, B, C) in enumerate(result):
    print(f"Компонента {i+1}:")
    print(f"A: {A}")
    print(f"B: {B}") 
    print(f"C: {C}\n")
import pickle


matrices1 = [[[1, 2], [3, 4]], [[5, 6], [7, 8]]]
matrices2 = [[[2, 0], [1, 2]], [[1, 1], [0, 1]]]

with open('file1.dat', 'wb') as f:
    pickle.dump(matrices1, f)
with open('file2.dat', 'wb') as f:
    pickle.dump(matrices2, f)
