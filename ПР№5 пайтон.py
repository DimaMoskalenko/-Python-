# --- Створення словника ---
students = {
    "Vitaly_Prikhodko": [12, 10, 9, 10, 5, 7, 8, 5, 12, 10, 11, 9],
    "Dmytro_Kropyvnytskyi": [12, 10, 9, 5, 6, 7, 4, 3, 12, 4, 6, 8],
    "Mikhail_Romanenko": [12, 3, 4, 6, 5, 5, 3, 7, 5, 4, 6, 5],
    "Maxim_Derizemlya": [12, 4, 10, 7, 5, 8, 3, 3, 5, 7, 9, 6],
    "Victoria_Zhuk": [10, 10, 10, 9, 10, 9, 10, 8, 7, 12, 11, 10],
    "Andrey_Kuryanov": [5, 6, 7, 5, 4, 7, 5, 4, 4, 8, 6, 7],
    "Oksana_Dubovets": [7, 8, 5, 8, 8, 9, 8, 7, 7, 10, 8, 9],
    "Nikita_Stroganov": [6, 7, 8, 9, 10, 10, 10, 10, 10, 9, 10, 9],
    "Karina_Nikolaenko": [2, 3, 5, 4, 5, 4, 3, 3, 5, 8, 6, 4],
    "Eugenia_Dron": [12, 12, 12, 10, 10, 9, 8, 9, 9, 8, 11, 10]
}
# --- Функція виведення всіх значень словника ---
def Print(students):
    for i in students:
        print("Оцінки", i, "-", students[i])
# --- Функція додавання нового учня ---
def add(students, key, grades):
    students[key] = grades
    print("Додано", key, ".")
# --- Функція видалення учня ---
def Del(students, key):
    try:
        del students[key]
        print("Видалено", key, ".")
    except KeyError:
        print("Помилка: учня з таким ім’ям немає у списку!")
# --- Функція сортування словника за прізвищем ---
def print_sort(students):
    students = {k: students[k] for k in sorted(students)}
    print("Відсортований словник:")
    for i in students:
        print("Оцінки", i, "-", students[i])
# --- Функція обчислення середніх оцінок ---
def calculate_average(students):
    averages = {}
    for name, grades in students.items():
        averages[name] = round(sum(grades) / len(grades), 2)
    class_avg = round(sum(averages.values()) / len(averages), 2)
    print("\nСередні оцінки учнів:")
    for name in averages:
        print(name, "-", averages[name])
    print("\nСередній бал по класу:", class_avg)
    print("\nУчні, у яких середній бал вищий за середній по класу:")
    for name, avg in averages.items():
        if avg > class_avg:
            print("⭐", name, "-", avg)
# --- Основна частина програми ---
while True:
    print("\n=== МЕНЮ ===")
    print("1 - Вивести всі оцінки учнів")
    print("2 - Додати нового учня")
    print("3 - Видалити учня")
    print("4 - Відсортувати учнів за прізвищем")
    print("5 - Порахувати середні оцінки")
    print("0 - Вихід")
    choice = input("Ваш вибір: ")
    if choice == "1":
        Print(students)
    elif choice == "2":
        name = input("Введіть прізвище_ім'я нового учня: ")
        try:
            grades = list(map(int, input("Введіть 12 оцінок через пробіл: ").split()))
            if len(grades) != 12:
                raise ValueError("Потрібно ввести саме 12 оцінок!")
            add(students, name, grades)
        except ValueError as e:
            print("Помилка:", e)
    elif choice == "3":
        name = input("Введіть ім’я учня для видалення: ")
        Del(students, name)
    elif choice == "4":
        print_sort(students)
    elif choice == "5":
        calculate_average(students)
    elif choice == "0":
        print("Програма завершена.")
        break
    else:
        print("Невірний вибір, спробуйте ще раз.")