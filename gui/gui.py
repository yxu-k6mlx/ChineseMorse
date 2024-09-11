import tkinter as tk
from parts.ButtonBar import ButtonBar
from parts.StringBox import StringBox
from parts.OutputBox import OutputBox

class MainWindow(tk.Frame): 
    def __init__(self, root, width=1200, height=700):
        tk.Frame.__init__(self, root, width=width, height=height, background='white') 

        self.sb = StringBox(self)
        self.sb.grid(column=0, row=0)

        self.bb = ButtonBar(self)
        self.bb.grid(column=0, row=1)

        self.ob = OutputBox(self)
        self.ob.grid(column=0, row=2)
        self.ob.set_text()

        return None 

if __name__ == '__main__': 
    root = tk.Tk()
    root.geometry('1200x700')
    main_window = MainWindow(root)
    main_window.place(x=0, y=0)

    tk.mainloop()