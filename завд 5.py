def single_letters():
    A = input("Введи текст з латинських літер: ")
    B = A.lower()
    print("Текст:", B)
    S = set(B)
    result = []
    for ch in S:
        if B.count(ch) == 1:
            result.append(ch)
    print("Символи, що зустрічаються один раз:")
    print(set(result))
    return result
single_letters()