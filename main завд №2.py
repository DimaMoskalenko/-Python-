N = 30
suma = 0
k = 0
print("i", "     ", "Сума")
for i in range(1, N + 1):
    suma += 1 / i
    k += 1
    if i < 10:
        print(i, " " * 6, round(suma, 5))
    else:
        print(i, " " * 5, round(suma, 5))
print("\nКількість членів ряду:", k)
print("Сума ряду:", round(suma, 5))