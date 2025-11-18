import matplotlib.pyplot as plt
import numpy as np
# Створюємо масив x від 0.01 до 10 (щоб уникнути 0^cos(0))
x = np.linspace(0.01, 10, 100)
# Обчислюємо Y(x)
y = -x**np.cos(5*x)
# Побудова графіка
plt.plot(x, y, label='Y(x) = -x^cos(5x)', color='green', linewidth=3)  # зелена лінія, товщина 3
# Назва графіка
plt.title('Графік функції Y(x) = -x^cos(5x)', fontsize=15)
# Позначення осей
plt.xlabel('x', fontsize=12, color='blue')
plt.ylabel('Y(x)', fontsize=12, color='blue')
# Легенда
plt.legend()
# Сітка
plt.grid(True)
# Показати графік
plt.show()