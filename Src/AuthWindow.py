import tkinter as tk
import ttkbootstrap as ttk
from bdrequests import BDRequests
from MainWindow import MainWindow

class Auth:
    def __init__(self, root):
        self.root = root
        self.root.title('Авторизация')
        self.BD = BDRequests()
        self.AuthWindow()
        self.root.mainloop()
        

    def login(self):
        login = self.login_entry.get()
        password = self.password_entry.get()
        auth_result = self.BD.auth(login,password)
        if auth_result:
            print("Авторизация прошла успешно")
            self.ClearWindow()
            MainWindow(self.root)
        else:
            self.message_label.configure(text="Неправильный логин или пароль")
            self.message_label.grid(row=2,columnspan=2)

            print("Неправильный логин или пароль")

    def signup(self):
        login = self.login_entry.get()
        password = self.password_entry.get()
        reg_result = self.BD.signup(login,password)
        if reg_result:
            print("Авторизация прошла успешно")
            self.ClearWindow()
            MainWindow(self.root)

        else:
            self.message_label.configure(text="Пользователь уже существует")
            self.message_label.grid(row=2,columnspan=2)

    def registration(self):
        self.message_label.grid_forget()
        self.title_label.configure(text='Регистрация')
        self.login_button.grid_forget()
        self.reg_button.grid_forget()
        self.signup_button = ttk.Button(self.login_frame, text='Зарегестрироваться',bootstyle="success", command=self.signup)
        self.signup_button.grid(row=6,columnspan=2,sticky="ew",pady=(10,0))

    def ClearWindow(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def AuthWindow(self):
        self.login_frame = tk.Frame(self.root)

        self.title_label = tk.Label(self.login_frame, text='Авторизация', font=('Arial', 17))
        self.login_label = tk.Label(self.login_frame, text='Имя пользователя', font=('Arial', 14))
        self.message_label = ttk.Label(self.login_frame, text="",bootstyle="danger")
        self.login_entry = tk.Entry(self.login_frame, font=('Arial', 14))
        self.password_label = tk.Label(self.login_frame, text='Пароль', font=('Arial', 14))
        self.password_entry = tk.Entry(self.login_frame, font=('Arial', 14), show='*')
        self.login_button = ttk.Button(self.login_frame, text='Войти',bootstyle="success", command=self.login)
        self.reg_button = ttk.Button(self.login_frame, text='Зарегестрироваться',bootstyle="info", command=self.registration)

        self.title_label.grid(row=0,columnspan=2)
        self.login_label.grid(row=1,columnspan=2, pady=(20,0))
        self.login_entry.grid(row=3,columnspan=2)
        self.password_label.grid(row=4,columnspan=2, pady=(5,0))
        self.password_entry.grid(row=5,columnspan=2)
        self.login_button.grid(row=6,columnspan=2,sticky="ew",pady=(10,0))
        self.reg_button.grid(row=7,columnspan=2,sticky="ew",pady=5)

        self.login_frame.place(relx=0.5, rely=0.4, anchor=tk.CENTER)

