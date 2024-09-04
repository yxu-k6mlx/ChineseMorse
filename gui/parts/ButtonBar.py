import tkinter as tk

class Bar(tk.Frame): 
    def __init__(self, root, top_buttons, bottom_buttons): 
        self.tk = root 
        self._w = tk.Canvas(self, bg='red', width=1600, height=200)
        self.top_buttons = top_buttons
        self.bottom_buttons = bottom_buttons

    def display_buttons(self, v): 
        if v: print(f'2-row bar: display buttons called')
        for col in range (0, len(self.top_buttons)): 
            self.top_buttons[col].grid(column=col, row=0)
            self.bottom_buttons[col].grid(column=col, row=1)
    
class Bar(tk.Frame): 
    def __init__(self, root, buttons): 
        self.tk = root 
        self._w = tk.Canvas(self, bg='red', width=1600, height=200)
        self.buttons = buttons 
    
    def display_buttons(self, v): 
        if v: print(f'1-row bar: display buttons called')
        for col in range (0, len(self.buttons)): 
            self.buttons[col].grid(column=col)


