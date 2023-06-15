import tkinter as tk
import ttkbootstrap as ttk
from bdrequests import BDRequests
import AuthWindow 

class MainWindow:
    def __init__(self, root):
        self.root = root
        self.root.title('Недвижимость')
        self.logoutbutton = ttk.Button(root, text="Выход", bootstyle="danger", command=self.logout)
        self.logoutbutton.pack(anchor="ne")
        self.title_label = tk.Label(self.root, text='Welcome', font=('Arial', 17))
        self.title_label.pack(expand=1)

    
    def logout(self):
        self.logoutbutton.destroy()
        AU = AuthWindow.Auth(self.root)
        AU.AuthWindow()
