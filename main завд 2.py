word = str(input("Введіть слово: "))
while len(word) == 0:
    word = str(input("Введіть слово ще раз, воно не може бути порожнім: "))
count = 0
for i in range(len(word)):
    if word[i] == "_":
        count += 1
print("Кількість символів '_' у слові =", count)