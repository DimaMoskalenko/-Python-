import matplotlib.pyplot as plt
import numpy as np
# Дані результатів (можна вставити прямо сюди)
result = {
    "ClassAverage": 7.9818181818181815,
    "AboveAverage": [
        "Іваненко",
        "Шевченко",
        "Сидоренко",
        "Коваль",
        "Ткаченко",
        "Лисенко"
    ]
}
above_avg = result["AboveAverage"]
total_students = 10
below_avg_count = total_students - len(above_avg)
data = [len(above_avg), below_avg_count]
labels = ["Вище середньої", "Нижче або рівно середньої"]
fig, ax = plt.subplots(figsize=(6, 3), subplot_kw=dict(aspect="equal"))
def func(pct, allvals):
    absolute = int(np.round(pct/100.*np.sum(allvals)))
    return f"{pct:.1f}%\n({absolute} уч.)"
wedges, texts, autotexts = ax.pie(data, autopct=lambda pct: func(pct, data),
                                  textprops=dict(color="w"), colors=["lightgreen", "lightcoral"])
ax.legend(wedges, labels,
          title="Групи учнів",
          loc="center left",
          bbox_to_anchor=(1, 0, 0.5, 1))
plt.setp(autotexts, size=8, weight="bold")
ax.set_title("Розподіл учнів за середньою оцінкою")
plt.show()