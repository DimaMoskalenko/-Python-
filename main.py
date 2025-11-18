import json
# Початкові дані учнів (10 учнів, 5 предметів)
students = [
    {"Surname": "Іваненко", "Grades": [8, 9, 10, 7, 9]},
    {"Surname": "Петренко", "Grades": [7, 6, 8, 7, 7]},
    {"Surname": "Шевченко", "Grades": [10, 9, 11, 10, 12]},
    {"Surname": "Бондар", "Grades": [5, 7, 6, 7, 6]},
    {"Surname": "Сидоренко", "Grades": [9, 9, 8, 10, 9]},
    {"Surname": "Коваль", "Grades": [11, 11, 10, 12, 10]},
    {"Surname": "Мельник", "Grades": [6, 7, 8, 6, 7]},
    {"Surname": "Ткаченко", "Grades": [9, 8, 9, 10, 7]},
    {"Surname": "Лисенко", "Grades": [10, 10, 9, 11, 10]},
    {"Surname": "Олійник", "Grades": [7, 8, 7, 8, 7]}
]
# Імена файлів
FILE_NAME = "grades.json"
RESULT_FILE = "result.json"
# Запис початкових даних у JSON
with open(FILE_NAME, "w", encoding="utf-8") as f:
    json.dump(students, f, ensure_ascii=False, indent=4)
# Функції для роботи з JSON
def load_data():
    with open(FILE_NAME, "r", encoding="utf-8") as f:
        return json.load(f)
def save_data(data):
    with open(FILE_NAME, "w", encoding="utf-8") as f:
        json.dump(data, f, ensure_ascii=False, indent=4)
# 1. Переглянути всіх учнів
def view_students():
    data = load_data()
    print("\n--- Учні та їхні оцінки ---")
    for s in data:
        print(f"{s['Surname']}: {s['Grades']}")
    print()
# 2. Додати учня
def add_student():
    data = load_data()
    surname = input("Прізвище учня: ")
    grades_input = input("Введіть 5 оцінок через пробіл: ")
    grades = list(map(int, grades_input.split()))
    if len(grades) != 5:
        print("❌ Помилка: потрібно ввести 5 оцінок!")
        return
    data.append({"Surname": surname, "Grades": grades})
    save_data(data)
    print("✅ Учня додано!\n")
# 3. Розрахунок середніх оцінок
def calculate_average():
    data = load_data()
    # середня кожного учня
    for s in data:
        s["Average"] = sum(s["Grades"]) / len(s["Grades"])
    # середня класу
    class_avg = sum(s["Average"] for s in data) / len(data)
    print(f"\nСередня оцінка класу: {class_avg:.2f}")
    # учні з середньою вище класної
    above_avg = [s["Surname"] for s in data if s["Average"] > class_avg]
    print("Учні з оцінками вище середньої класу:")
    for s in above_avg:
        print(" -", s)
    # запис у файл
    with open(RESULT_FILE, "w", encoding="utf-8") as f:
        json.dump({"ClassAverage": class_avg, "AboveAverage": above_avg}, f, ensure_ascii=False, indent=4)
    print("\n✅ Результат збережено у result.json\n")
# Меню
while True:
    print("Меню:\n 1 - Переглянути всіх учнів\n 2 - Додати учня\n 3 - Розрахувати середні оцінки\n 4 - Вихід")
    choice = input("Ваш вибір: ")
    if choice == "1":
        view_students()
    elif choice == "2":
        add_student()
    elif choice == "3":
        calculate_average()
    elif choice == "4":
        break
    else:
        print("❌ Помилка: такої опції нема\n")