import wbdata
import pandas as pd
import sys
# ---- Параметри ----
start_year = 2018
end_year = 2019
indicator_code = "NE.EXP.GNFS.ZS"
input_filename = "exports_2018_2019.csv"
output_filename = "search_results.csv"
def download_data():
    print("Завантаження даних World Bank через wbdata...")
    indicator = {indicator_code: "Exports % GDP"}
    try:
        # Отримуємо всі дані без convert_date
        df = wbdata.get_dataframe(indicator, country="all")
        if df.empty:
            print("❌ Дані не знайдено. Перевірте індикатор.")
            sys.exit(1)
        # Робимо reset_index для country та date
        df = df.reset_index()
        # Конвертуємо date у datetime
        df['date'] = pd.to_datetime(df['date'], errors='coerce')
        # Видаляємо рядки з неконвертованими датами
        df = df.dropna(subset=['date'])
        # Фільтруємо роки 2018 та 2019
        df['year'] = df['date'].dt.year
        df = df[df['year'].isin([start_year, end_year])]
        return df
    except Exception as e:
        print("❌ Помилка при завантаженні даних:", e)
        sys.exit(1)
def prepare_csv(df):
    # Повертаємо країни як індекс і роки як стовпці
    df_pivot = df.pivot(index="country", columns="year", values="Exports % GDP")
    df_pivot.index.name = "Country"
    return df_pivot
def save_csv(df, filename):
    try:
        df.to_csv(filename, encoding="utf-8")
        print(f"✅ CSV збережено у '{filename}'")
    except Exception as e:
        print("❌ Помилка при збереженні CSV:", e)
        sys.exit(1)
def print_csv_head(df, n=20):
    print(f"\n--- Перші {n} рядків CSV ---")
    print(df.head(n))
    print("--- кінець виводу ---\n")
def search_countries(df, queries):
    queries_lower = [q.strip().lower() for q in queries if q.strip()]
    if not queries_lower:
        return pd.DataFrame(columns=df.columns)
    mask = df.index.to_series().apply(lambda x: any(q in x.lower() for q in queries_lower))
    return df[mask]
def main():
    df_raw = download_data()
    df_csv = prepare_csv(df_raw)
    save_csv(df_csv, input_filename)
    print_csv_head(df_csv, n=20)
    # Ввід користувача
    print("Введіть назви країн для пошуку (через кому), приклад: Ukraine, Poland, United States")
    user_input = input("Країни: ")
    queries = [q.strip() for q in user_input.split(",")]
    df_search = search_countries(df_csv, queries)
    # Збереження результатів
    try:
        df_search.to_csv(output_filename, encoding="utf-8")
        print(f"✅ Результати пошуку збережено у '{output_filename}'. Знайдено рядків: {len(df_search)}")
    except Exception as e:
        print("❌ Помилка при записі результатів:", e)
        sys.exit(1)
    # Вивід результатів пошуку
    if not df_search.empty:
        print("\n--- Результати пошуку ---")
        print(df_search)
        print("--- кінець результатів ---")
    else:
        print("⚠️ Не знайдено жодної країни за введеними назвами.")
if __name__ == "__main__":
    main()