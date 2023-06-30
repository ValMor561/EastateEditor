import tkinter as tk
import ttkbootstrap as ttk
from bdrequests import BDRequests
from Tree import Tree
from SearchFrame import SearchFrame

class MainWindow:
    def __init__(self, root, username):
        self.root = root
        self.root.title('Недвижимость')
        self.BD = BDRequests()
        self.page = 1
        self.SR = SearchFrame(root, "get_object_type", username)
        self.NotebookWindow()
        
    def NotebookWindow(self):
        self.notebook = ttk.Notebook(self.root,bootstyle="success")
        self.notebook.pack(fill='both', expand=True)

        entities = {'Объекты недвижимости' : ["ObjectId",'Адресс', 'Площадь', 'Тип объекта', 'Район', 'Город', 'Фамилия владельца', 'Имя владельца'], 'Данные клиентов' : ["PsId", 'Фамилия', 'Имя', 'Номер паспорта','Код отделения', 'Дата рождения', 'Город', 'Возраст', 'Семейное положение'], 'Контракты' : ["ContacrId", 'Дата подписания', 'Дата выплаты', 'Стоимость', 'Тип контракта','Фамилия риелтора', 'Фамилия владельца', 'Имя владельца', 'Фамилия покупателя', 'Имя покупателя'], 'Сотрудники': ["Id", 'Фамилия', 'Имя', 'Имя компании']}
        function = {'Объекты недвижимости' : ['get_real_eastate', 'delete_eastate', 'update_real_estate_object', 'add_real_estate_object', 'block_reo'], 'Данные клиентов' : ['get_passport_client', 'delete_client', 'update_passport', 'add_passport' , 'block_passport'], 'Контракты' : ['get_contract','delete_contract', 'update_contract', 'add_contract', 'block_contract'], 'Сотрудники': ['get_employee','delete_employee', 'update_employee', 'add_employee' , 'block_employee']}
        for entity in entities:
            self.frame = ttk.Frame(self.notebook)
            self.notebook.add(self.frame,text=entity)

            self.Tree = Tree(self.frame, entities[entity], self.page, function[entity], entity)
    
    