import tkinter as tk
import ttkbootstrap as ttk
from bdrequests import BDRequests
from Edit import EditForm

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
        self.tree.heading("hidden", text="Hidden Column")
        for col in self.columns[1:]:
            self.tree.heading(col, text=col)
            self.tree.column(col, anchor="center")
        self.tree['displaycolumns'] = self.columns[1:]

        data = self.BD.get_data(self.page, self.function)
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
        popMenu.add_command(label="Edit", command=lambda: self.OpenEditForm(self.columns[1:], row_values[1:]))
        popMenu.add_command(label="Delete") 
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
    
    def OpenEditForm(self, columns, row_values):
        # Создаем окно и отображаем форму редактирования
        edit_form = EditForm(columns, row_values)
        edit_form.grab_set()
        edit_form.wait_window()