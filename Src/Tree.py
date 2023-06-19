import tkinter as tk
import ttkbootstrap as ttk
from bdrequests import BDRequests

class Tree():
    def __init__(self,frame, columns, page, function):
        self.frame = frame
        self.function = function
        self.columns = columns
        self.page = page
        self.BD = BDRequests()
        self.Tree()
        self.PageButtons()
        
    def Tree(self):
        self.tree = ttk.Treeview(self.frame, columns=self.columns,show='headings',bootstyle='light')
        for col in self.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")

        data = self.BD.get_data(self.page, self.function)
        for row in data:
            self.tree.insert('', tk.END, values=row[1:])

        self.tree.pack(fill='both', expand=True)
        
    def PageButtons(self):
        self.page_frame = ttk.Frame(self.frame)
        self.page_frame.pack(side="bottom", pady=(0,50))

        self.prev_button = tk.Button(self.page_frame, text="< Предыдующая", command=self.PrevPage)
        self.prev_button.pack(side=tk.LEFT)

        self.page_label = tk.Label(self.page_frame, text=self.page)
        self.page_label.pack(side=tk.LEFT)

        self.next_button = tk.Button(self.page_frame, text="Следующая >", command=self.NextPage)
        self.next_button.pack(side=tk.LEFT)

    def ClearFrame(self):
        for widget in self.frame.winfo_children():
            widget.destroy()

    def PrevPage(self):
        if self.page > 1:
            self.page -= 1
            self.ClearFrame()
            self.Tree()
            self.PageButtons()
    
    def NextPage(self):
        self.page += 1
        self.ClearFrame()
        self.Tree()
        self.PageButtons()
            