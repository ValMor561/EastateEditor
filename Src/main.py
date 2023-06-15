from AuthWindow import Auth
import ttkbootstrap as ttk

root = ttk.Window(themename="darkly")
root.geometry('900x900')
Auth(root)