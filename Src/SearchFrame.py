import tkinter as tk
import ttkbootstrap as ttk
from bdrequests import BDRequests
import AuthWindow 

class SearchFrame():
    def __init__(self, root, function, username):
        self.search_frame = ttk.Frame()
        self.search_frame.pack(side=tk.TOP, fill=tk.X)
        self.function = function
        self.username = username
        self.BD = BDRequests()
        self.root = root
        self.PaintFrame()

    def PaintFrame(self):
        logoutbutton = ttk.Button(self.search_frame, text="Выход", bootstyle="danger", command=self.logout)
        logoutbutton.pack(side=tk.RIGHT, padx=(0,10))
        
        usernamebtn = ttk.Button(self.search_frame, text=self.username, bootstyle="success",padding=(30,5,30,5), state='disabled')
        usernamebtn.pack(side=tk.RIGHT)
        
        ttk.Button(self.search_frame, text="Найти").pack(side=tk.RIGHT, pady=5)
        
        options = self.BD.getValues("get_family")
        dropdown = ttk.Combobox(self.search_frame, values=options,  height=4, state="readonly")
        dropdown.pack(side=tk.RIGHT)

        ttk.Label(self.search_frame, text="Фильтр по:", font=('Arial', 14)).pack(side=tk.RIGHT) 

    def logout(self):
        self.BD.audit(self.username,"Выход")
        self.ClearWindow()
        AU = AuthWindow.Auth(self.root)
        AU.AuthWindow()            

    def ClearWindow(self):
        for widget in self.root.winfo_children():
            widget.destroy()

