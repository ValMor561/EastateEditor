import tkinter as tk
import ttkbootstrap as ttk
from bdrequests import BDRequests
from datetime import datetime

class EditOrAddForm(tk.Toplevel):
    def __init__(self, row_values, updatefunction, addfunction, blockfunction):
        super().__init__()
        self.resizable(width=False, height=False)
        self.title("Форма Изменения/Добавления")
        self.id = row_values[0]
        self.values = row_values[1:]
        self.updatefunction = updatefunction
        self.addfunction = addfunction
        self.blockfunction = blockfunction
        self.BD = BDRequests()
        self.BD.block_data(self.blockfunction,self.id)
        self.entries = []
    
    def Contract(self):
        self.LabelCalendar("Дата контракта", 0)
        self.LabelCalendar("Дата выплаты", 1)
        self.LabelEntry("Стоимость", 2)
        self.LabelDropMenu("Тип контракта", "get_contract_types", 3)
        self.LabelDropMenu("Номер риелтора", "get_employee_number", 4)
        self.LabelDropMenu("Паспорт владельца", "get_passports", 5)
        self.LabelDropMenu("Паспорт покупателя", "get_passports", 6)

        save_button = tk.Button(self, text="Сохранить", command=self.save)
        save_button.grid(row=7, columnspan=2, padx=5, pady=5)

    def Employee(self):
        self.LabelEntry("Фамилия", 0)
        self.LabelEntry("Имя", 1)
        self.LabelDropMenu("Имя компании", "get_company_name", 2)

        save_button = tk.Button(self, text="Сохранить", command=self.save)
        save_button.grid(row=5, columnspan=2, padx=5, pady=5)

    def Client(self):
        columns = ['Фамилия', 'Имя', 'Номер паспорта','Код отделения'] 
        i = 0
        for col in columns:
            self.LabelEntry(col,i)
            i += 1
        self.LabelCalendar("Дата рождения", i)
        i += 1
        columns = ['Город', 'Возраст']
        for col in columns:
            self.LabelEntry(col,i)
            i += 1
        self.LabelDropMenu("Семейное положение", "get_family", i)

        save_button = tk.Button(self, text="Сохранить", command=self.save)
        save_button.grid(row=i+1, columnspan=2, padx=5, pady=5)

    def Eastate(self):
        self.LabelEntry("Адресс", 0)
        self.LabelEntry("Площадь", 1)
        self.LabelDropMenu("Тип объекта", "get_object_type",2)
        self.LabelDropMenu("Номер района", "get_districtid", 3)
        self.LabelDropMenu("Паcпорт владельца", "get_passports", 4)
        
        save_button = tk.Button(self, text="Сохранить", command=self.save)
        save_button.grid(row=5, columnspan=2, padx=5, pady=5)
    
    def LabelCalendar(self, text, index):
        label = tk.Label(self, text=text)
        label.grid(row=index, column=0, padx=5, pady=5)

        if self.values[index] == "":
            self.values[index] = datetime.now().strftime("%Y-%m-%d")

        data_entry = ttk.DateEntry(self, startdate=datetime.strptime(self.values[index], "%Y-%m-%d"))
        data_entry.configure(state="readonly")
        data_entry.grid(row=index, column=1, padx=5, pady=5)
        self.entries.append(data_entry)
        return data_entry

    def LabelDropMenu(self, text, functions, index):
        label = tk.Label(self, text=text)
        label.grid(row=index, column=0, padx=5, pady=5)
        options = self.BD.getValues(functions)
        dropdown = ttk.Combobox(self, values=options,  height=4, state="readonly")
        dropdown.grid(row=index, column=1, padx=5, pady=5)
        self.entries.append(dropdown)
        return dropdown

    def LabelEntry(self, text, index):
        label = tk.Label(self, text=text)
        label.grid(row=index, column=0, padx=5, pady=5)
        entry = tk.Entry(self)
        entry.insert(0, self.values[index])
        entry.grid(row=index, column=1, padx=5, pady=5)
        self.entries.append(entry)
        return entry

    def save(self):
        values = []
        for entry in self.entries:
            if isinstance(entry, ttk.DateEntry):
                values.append(entry.entry.get())
                continue
            values.append(entry.get())
        if self.id != "":
            self.BD.edit_data(self.updatefunction, self.id, values)
        else:
            self.BD.add_data(self.addfunction, values)
        self.destroy()
        return values
