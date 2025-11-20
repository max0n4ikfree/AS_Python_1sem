if __name__ == "__main__":
    pass
with open('dates.txt') as f:
    for line in f:
        day, month, year = map(int, line.split())
        if 3 <= month <= 5:
            print(f"{day:02d}.{month:02d}.{year}")
