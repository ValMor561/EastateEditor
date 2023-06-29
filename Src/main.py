from AuthWindow import Auth
import ttkbootstrap as ttk

def main(): 
    root = ttk.Window(themename="superhero")
    root.geometry('1920x1080')
    Auth(root)
    root.mainloop()

if __name__ == "__main__":
    main()