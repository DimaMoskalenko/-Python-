a = int(input("Введіть a: "))
while (a < 1 or a > 100):
    a = int(input("Введіть a (від 1 до 100): "))
b = int(input("Введіть b: "))
while (b < 1 or b > 100):
    b = int(input("Введіть b (від 1 до 100): "))
if a > b:
    r = a / b + 1
elif a == b:
    r = -2
else:
    r = (a - b) / a
print("Результат обчислення виразу: ", r)