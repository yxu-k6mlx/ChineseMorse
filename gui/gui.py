import tkinter as tk
from gui.parts.ButtonBar import ButtonBar as ButtonBar
from gui.parts.StringBox import StringBox as StringBox
from gui.parts.OutputBox import OutputBox as OutputBox

class MainWindow(tk.Frame): 
    def __init__(self, root, width=1200, height=700, gui_cmds=[None]*4):
        tk.Frame.__init__(self, root, width=width, height=height, background='white') 
        
        self.sb = StringBox(self)
        self.sb.grid(column=0, row=0)

        self.bb = ButtonBar(self, btncmds=gui_cmds)
        self.bb.grid(column=0, row=1)

        self.ob = OutputBox(self)
        self.ob.grid(column=0, row=2)
        self.ob.set_text(input='')

        return None 

if __name__ == '__main__': 
    root = tk.Tk()
    root.geometry('1200x700')
    root.title('Chinese Morse Tool')
    main_window = MainWindow(root)
    main_window.place(x=0, y=0)

    tk.mainloop()