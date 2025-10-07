n = 7
a = [[7 - abs(i - j) for j in range(n)] for i in range(n)]
for row in a:
    print(*row)