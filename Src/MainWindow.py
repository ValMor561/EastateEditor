import tkinter as tk
import ttkbootstrap as ttk
from bdrequests import BDRequests
import AuthWindow 

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title('Недвижимость')
        
        self.SearchFrame()
        self.NotebookWindow()
        
        
    def NotebookWindow(self):

        tab = ttk.Notebook(bootstyle="success")
        entities = {'Объекты недвижимости' : ['Адресс', 'Площадь', 'Тип объекта', 'Район', 'Город', 'Фамилия владельца', 'Имя владельца'], 'Данные клиентов' : ['Фамилия', 'Имя', 'Номер паспорта','Код отделения', 'Дата рождения', 'Город', 'Возраст', 'Семейное положение'], 'Сотрудники':['Фамилия', 'Имя', 'Имя компании']}
        for entity in entities:
            frame = ttk.Frame(tab)
            tab.add(frame,text=entity)

            data_grid = ttk.Treeview(frame, columns=entities[entity],show='headings',bootstyle='light')

            for col in entities[entity]:
                data_grid.heading(col, text=col)    
                
            data_grid.pack(fill=tk.BOTH, expand=True)
        
        tab.pack(fill=tk.BOTH, expand=True)

    def ClearWindow(self):
        for widget in self.root.winfo_children():
            widget.destroy()


    def logout(self):
        self.ClearWindow()
        AU = AuthWindow.Auth(self.root)
        AU.AuthWindow()

    def SearchFrame(self):
            search_frame = ttk.Frame()
            search_frame.pack(side=tk.TOP, fill=tk.X)
            
            logoutbutton = ttk.Button(search_frame, text="Выход", bootstyle="danger", command=self.logout)
            logoutbutton.pack(side=tk.RIGHT, padx=(5,10))

            ttk.Button(search_frame, text="Найти").pack(side=tk.RIGHT, pady=5)
            
            search_entry = ttk.Entry(search_frame)
            search_entry.pack(side=tk.RIGHT)

            ttk.Label(search_frame, text="Поиск:", font=('Arial', 14)).pack(side=tk.RIGHT) 