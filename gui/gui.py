import tkinter as tk

class MainWindow(tk.Frame): 
    def __init__(self, root, width=800, height=600):
        tk.Frame.__init__(self, root, width=width, height=height, background='red') 
        return None 

if __name__ == '__main__': 
    root = tk.Tk() 
    main_window = MainWindow(root)
    main_window.grid(column=0, row=0)

    tk.mainloop()