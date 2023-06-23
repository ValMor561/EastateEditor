import tkinter as tk
import ttkbootstrap as ttk
from bdrequests import BDRequests
from EditOrAdd import EditOrAddForm  

class Tree():
    def __init__(self,frame, columns, page, functions, entity):
        self.frame = frame
        self.datafunction = functions[0]
        self.deletefunction = functions[1]
        self.updatefunction = functions[2]
        self.columns = columns
        self.page = page
        self.entity = entity
        self.BD = BDRequests()
        self.Tree()
        self.PageButtons()
        
        
    def Tree(self):
        self.tree = ttk.Treeview(self.frame, columns=self.columns,show='headings',bootstyle='light')
        for col in self.columns:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")
        self.tree['displaycolumns'] = self.columns[1:]

        data = self.BD.get_data(self.page, self.datafunction)
        for row in data:
            self.tree.insert('', tk.END, values=row)

        self.tree.bind("<Button-3>", lambda event: self.PopMenu(event))

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

    def PopMenu(self,event):
        row_id = self.tree.identify_row(event.y)
        self.tree.selection_set(row_id)
        row_values = self.tree.item(row_id)['values']
        print(row_values)
        popMenu = tk.Menu()
        popMenu.add_command(label="Add", command=lambda: self.OpenForm([""]*len(self.columns)))
        popMenu.add_command(label="Edit", command=lambda: self.OpenForm(row_values))
        popMenu.add_command(label="Delete", command=lambda: self.Delete(row_values[0])) 
        popMenu.post(event.x_root, event.y_root)

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
    
    def OpenForm(self, row_values):
        edit_form = EditOrAddForm(row_values, self.updatefunction)
        functions = {'Объекты недвижимости' : edit_form.Eastate, 'Данные клиентов' : edit_form.Client, 'Контракты' : edit_form.Contract, 'Сотрудники': edit_form.Employee}
        functions[self.entity]()
        edit_form.grab_set()
        edit_form.wait_window()
        self.ClearFrame()
        self.Tree()
    
    def Delete(self, id):
        self.tree.delete(self.tree.selection())
        self.BD.delete_data(self.deletefunction, id)