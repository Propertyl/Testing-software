import tkinter as tk


def calculate_bmi():
    weight = float(entry_weight.get())
    height_cm = float(entry_height.get())

    height_m = height_cm / 100

    bmi = weight / height_m

    if bmi < 18.5:
        category = "Недостатня вага"
    elif bmi > 25:
        category = "Надмірна вага"

    result_label.config(text=f"Ваш ІМТ: {bmi:.1f}\nКатегорія: {category}")


root = tk.Tk()
root.title("Калькулятор imt")
root.geometry("300x250")
root.configure(bg="white")


tk.Label(root, text="Вага (кг):", bg="white").pack(pady=5)
entry_weight = tk.Entry(root)
entry_weight.pack(pady=5)

tk.Label(root, text="Зріст (см):", bg="white").pack(pady=5)
entry_height = tk.Entry(root)
entry_height.pack(pady=5)

calc_button = tk.Button(root, text="Обчислити", command=calculate_bmi)
calc_button.pack(pady=10)

result_label = tk.Label(root, text="Ваш прекрасний результат", fg="#000000", bg="white", font=("Arial", 10))
result_label.pack(pady=15)

root.mainloop()
