n = int(input("n = "))
print(f"Enter {n} array elements:")
arr = [float(input()) for _ in range(n)]
positive = [x for x in arr if x > 0]
if len(positive) > 0:
    avg = sum(positive) / len(positive)
    print("Average of positive elements =", avg)
else:
    print("No positive elements")