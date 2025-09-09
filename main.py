N = int(input("Введіть число N (1<N<9): "))
while N <= 1 or N >= 9:
    N = int(input("Неправильне число, введіть ще раз: "))
for i in range(1, N + 1):
    num = N
    for j in range(N, 0, -1):
        if j >= i:
            print(num, end="")
            num -= 1
        else:
            break
    print("")