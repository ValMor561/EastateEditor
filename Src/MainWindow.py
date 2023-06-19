import tkinter as tk
import ttkbootstrap as ttk
from bdrequests import BDRequests
import AuthWindow 
from Tree import Tree

class MainWindow:
    def __init__(self, root, username):
        self.root = root
        self.root.title('Недвижимость')
        self.username = username
        self.BD = BDRequests()
        self.page = 1
        self.SearchFrame()
        self.NotebookWindow()
        
    def NotebookWindow(self):
        self.notebook = ttk.Notebook(self.root,bootstyle="success")
        self.notebook.pack(fill='both', expand=True)

        entities = {'Объекты недвижимости' : ['Адресс', 'Площадь', 'Тип объекта', 'Район', 'Город', 'Фамилия владельца', 'Имя владельца'], 'Данные клиентов' : ['Фамилия', 'Имя', 'Номер паспорта','Код отделения', 'Дата рождения', 'Город', 'Возраст', 'Семейное положение'], 'Сотрудники': ['Фамилия', 'Имя', 'Имя компании']}
        function = {'Объекты недвижимости' : 'get_real_eastate', 'Данные клиентов' : 'get_passport_client', 'Сотрудники': 'get_employee'}
        for entity in entities:
            self.frame = ttk.Frame(self.notebook)
            self.notebook.add(self.frame,text=entity)

            self.Tree = Tree(self.frame, entities[entity], self.page, function[entity])
           
            

    def ClearWindow(self):
        for widget in self.root.winfo_children():
            widget.destroy()


    def logout(self):
        self.BD.audit(self.username,"Выход")
        self.ClearWindow()
        AU = AuthWindow.Auth(self.root)
        AU.AuthWindow()

    
    def SearchFrame(self):
            search_frame = ttk.Frame()
            search_frame.pack(side=tk.TOP, fill=tk.X)
            
            logoutbutton = ttk.Button(search_frame, text="Выход", bootstyle="danger", command=self.logout)
            logoutbutton.pack(side=tk.RIGHT, padx=(0,10))
            
            usernamebtn = ttk.Button(search_frame, text=self.username, bootstyle="success",padding=(30,5,30,5), state='disabled')
            usernamebtn.pack(side=tk.RIGHT)
            

            ttk.Button(search_frame, text="Найти").pack(side=tk.RIGHT, pady=5)
            
            search_entry = ttk.Entry(search_frame)
            search_entry.pack(side=tk.RIGHT)

            ttk.Label(search_frame, text="Поиск:", font=('Arial', 14)).pack(side=tk.RIGHT) 