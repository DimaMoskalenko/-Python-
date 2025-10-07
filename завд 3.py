def delete():
    A = list(map(int, input("Введи список чисел через пробіл: ").split()))
    print("Початковий список:", A)
    k = int(input("Введи індекс елемента для видалення: "))
    result = []
    for i in range(len(A)):
        if i != k:
            result.append(A[i])
    print("Список після видалення:", result)
    return result
delete()