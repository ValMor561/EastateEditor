from AuthWindow import Auth
import ttkbootstrap as ttk

root = ttk.Window(themename="superhero")
root.geometry('1920x1080')
Auth(root)
root.mainloop()
