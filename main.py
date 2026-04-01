import tkinter as tk


def calculate_bmi():
    # Отримуємо дані з полів (без перевірки на текст!)
    weight = float(entry_weight.get())
    height_cm = float(entry_height.get())

    height_m = height_cm / 100

    # Неправильна формула розрахунку
    bmi = weight / height_m

    # Неповні умови для категорій
    if bmi < 18.5:
        category = "Недостатня вага"
    elif bmi > 25:
        category = "Надмірна вага"

    # Виведення результату
    result_label.config(text=f"Ваш ІМТ: {bmi:.1f}\nКатегорія: {category}")


root = tk.Tk()
root.title("Калькулятор ІМТ")
root.geometry("300x250")
root.configure(bg="white")

# Кнопка знаходиться зверху, до полів вводу
calc_button = tk.Button(root, text="Розрахувати", command=calculate_bmi)
calc_button.pack(pady=10)

# Поля без вказівки одиниць виміру
tk.Label(root, text="Вага:", bg="white").pack(pady=5)
entry_weight = tk.Entry(root)
entry_weight.pack(pady=5)

tk.Label(root, text="Зріст:", bg="white").pack(pady=5)
entry_height = tk.Entry(root)
entry_height.pack(pady=5)

# Текст результату зливається з фоном
result_label = tk.Label(root, text="Тут буде ваш результат", fg="#f0f0f0", bg="white", font=("Arial", 10))
result_label.pack(pady=15)

root.mainloop()