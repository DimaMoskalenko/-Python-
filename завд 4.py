def second_elements():
    A = input("Введи список через пробіл: ").split()
    print("Початковий список:", A)
    result = A[1::2]
    print("Кожен другий елемент:", result)
    return result
second_elements()