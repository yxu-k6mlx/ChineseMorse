import tkinter as tk 
import tkinter.scrolledtext as st

class OutputBox(tk.Frame): 
    def __init__(self, root, width=1200, height=300): 
        tk.Frame.__init__(self, root, width=width, height=height) 

        self.frame = tk.Frame(
            self, 
            width=width, height=height, 
            background='#e57200'
        )
        
        self.obox = tk.Text(
            self.frame, 
            width=0, height=0, 
            #text='Placeholder Text', 
            background='#e57200', 
            foreground='black', 
            font=('Noto Sans SemiBold', 20), 
            #justify='left', 
            #anchor='nw', 
            padx=5, pady=5, 
            highlightbackground='black',
            highlightthickness=2
        )

        self.frame.grid(column=0, row=0)
        self.frame.grid_propagate(False)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)

        self.obox.grid(column=0, row=0)
        self.obox.grid(sticky='eswn')

        return None

    def set_text(self, input='GUI TEXT'): 
        #self.obox.configure(text=input)
        self.obox.insert(1.0, input)
        return True