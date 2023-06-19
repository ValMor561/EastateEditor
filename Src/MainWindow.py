import tkinter as tk
import ttkbootstrap as ttk
from bdrequests import BDRequests
import AuthWindow 

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
        self.tab = ttk.Notebook(self.root,bootstyle="success")
        self.tab.pack(fill='both', expand=True)

        entities = {'Объекты недвижимости' : ['Адресс', 'Площадь', 'Тип объекта', 'Район', 'Город', 'Фамилия владельца', 'Имя владельца'], 'Данные клиентов' : ['Фамилия', 'Имя', 'Номер паспорта','Код отделения', 'Дата рождения', 'Город', 'Возраст', 'Семейное положение'], 'Сотрудники':['Фамилия', 'Имя', 'Имя компании']}
        for entity in entities:
            self.frame = ttk.Frame(self.tab)
            self.tab.add(self.frame,text=entity)

            self.data_grid = ttk.Treeview(self.frame, columns=entities[entity],show='headings',bootstyle='light')
            

            for col in entities[entity]:
                self.data_grid.heading(col, text=col)
                self.data_grid.column(col, anchor="center")

            data = self.BD.get_REO(self.page)
            for row in data:
                self.data_grid.insert('', tk.END, values=row[1:])
            self.PageButtons()
            self.data_grid.pack(fill='both', expand=True)
        

    def ClearWindow(self):
        for widget in self.root.winfo_children():
            widget.destroy()


    def logout(self):
        self.BD.audit(self.username,"Выход")
        self.ClearWindow()
        AU = AuthWindow.Auth(self.root)
        AU.AuthWindow()

    def PageButtons(self):
        page_frame = ttk.Frame(self.data_grid)
        page_frame.pack(side="bottom")


        self.prev_button = tk.Button(page_frame, text="< Предыдующая", command=self.prev_page)
        self.prev_button.pack(side=tk.LEFT)

        self.page_label = tk.Label(page_frame, text=self.page)
        self.page_label.pack(side=tk.LEFT)

        self.next_button = tk.Button(page_frame, text="Следующая >", command=self.next_page)
        self.next_button.pack(side=tk.LEFT)

    def prev_page(self):
        if self.page > 1:
            self.page -= 1
            self.tab.destroy()
            self.NotebookWindow()

    def next_page(self):
        self.page += 1
        self.tab.destroy()
        self.NotebookWindow()

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