with open(r'C:\Users\asus\PycharmProjects\19\homework\dates.txt', 'r') as file:
    for line in file:
        parts = line.strip().split()
        if len(parts) >= 3:
            day = int(parts[0])
            month = int(parts[1])
            year = int(parts[2])

            if month == 3 or month == 4 or month == 5:
                print(f"{day:02d}.{month:02d}.{year}")

# Даты написал в новом файле (.txt), чтобы проверить программу:
15 3 2023
10 6 2022
25 4 2021
30 5 2022
