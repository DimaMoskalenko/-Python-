def series_sum(n):
    s = 0
    for i in range(1, n + 1):
        s += (i + 2) / (i + 1)
    return s