import tkinter as tk 

class OutputBox(tk.Frame): 
    def __init__(self, root, width=1200, height=300): 
        tk.Frame.__init__(self, root, width=0, height=0) 

        self.frame = tk.Canvas(self, width=width, height=height, background='#e57200')
        self.frame.grid(column=0, row=0)
        self.frame.grid_propagate(False)
        self.frame.rowconfigure(0, weight=1)
        self.frame.columnconfigure(0, weight=1)

        self.outbox = tk.Label(self, width=0, height=0, fg='black', bg='#e57200', justify='left', anchor='nw')
        self.outbox.place(x=2, y=2)
        
        return None 
    
    def set_text(self, input='Sample Text\nSample Line 2\n非ASCII字符測試\n{.....}'): 
        self.outbox.configure(text=input, font=('Noto Sans SemiBold', 20))

        return None 