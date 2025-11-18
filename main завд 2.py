import wbgapi as wb
import pandas as pd
import matplotlib.pyplot as plt
# Індикатор: Children out of school, primary (% of primary school age)
indicator = 'SE.PRM.UNER.ZS'
# Країни
countries = ['UKR', 'USA']
# Роки
years = list(range(2003, 2023))
# Завантажуємо дані у вигляді DataFrame
df = wb.data.DataFrame(indicator, economy=countries, time=years)
df = df.transpose()
df = df.rename_axis('Year').reset_index()
while True:
    # Меню для вибору завдання
    print("\nОберіть, що ви хочете зробити:")
    print("1 - Побудувати лінійний графік динаміки для України та США (пункт 2.1)")
    print("2 - Побудувати стовпчасту діаграму для вибраної країни (пункт 2.2)")
    print("3 - Вихід з програми")
    choice = input("Введіть номер (1, 2 або 3): ").strip()
    if choice == '1':
        # 2.1 Лінійний графік
        plt.figure(figsize=(10, 6))
        plt.plot(df['Year'], df['UKR'], marker='o', label='Ukraine')
        plt.plot(df['Year'], df['USA'], marker='s', label='USA')
        plt.title('Children out of school (% of primary school age) - Ukraine vs USA')
        plt.xlabel('Year')
        plt.ylabel('Percent of children out of school')
        plt.grid(True)
        plt.legend()
        plt.show()
    elif choice == '2':
        # 2.2 Стовпчаста діаграма
        country = input("Введіть код країни (UKR або USA): ").strip().upper()
        if country not in ['UKR', 'USA']:
            print("Країна не знайдена, будуємо для України")
            country = 'UKR'
        plt.figure(figsize=(10, 6))
        plt.bar(df['Year'], df[country], color='skyblue')
        plt.title(f'Children out of school (%) - {country}')
        plt.xlabel('Year')
        plt.ylabel('Percent of children out of school')
        plt.show()
    elif choice == '3':
        print("Програма завершена.")
        break
    else:
        print("Невірний вибір. Будь ласка, введіть 1, 2 або 3.")