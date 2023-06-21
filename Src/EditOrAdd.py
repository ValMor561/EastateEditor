import tkinter as tk
import ttkbootstrap as ttk

class EditOrAddForm(tk.Toplevel):
    def __init__(self, columns, row_values):
        super().__init__()
        self.resizable(width=False, height=False)

        self.title("Форма Изменения/Добавления")
        # Создаем поля формы на основе переданных колонок и значений строки
        self.entries = []
        for col, val in zip(columns, row_values):
            label = tk.Label(self, text=col)
            label.grid(row=len(self.entries), column=0, padx=5, pady=5)
            entry = tk.Entry(self)
            entry.insert(0, val)  # устанавливаем значение из row_values
            entry.grid(row=len(self.entries), column=1, padx=5, pady=5)
            self.entries.append(entry)

        # Добавляем кнопку "Сохранить"
        save_button = tk.Button(self, text="Сохранить", command=self.save)
        save_button.grid(row=len(self.entries), columnspan=2, padx=5, pady=5)

    def save(self):
        # Собираем значения из полей формы и передаем их обратно в основное окно
        values = [entry.get() for entry in self.entries]
        self.destroy()
        return values
