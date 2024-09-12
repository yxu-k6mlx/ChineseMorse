import tkinter as tk
from parts.SqButton import SqButton

class ButtonBar(tk.Frame): 
    def __init__(self, root, width=1200, height=100): 
        tk.Frame.__init__(self, root, width=width, height=height) 

        self.buttons = [None]*8
        
        self.buttons[0] = SqButton(
            root, self, text='LOAD INPUT\n載入文字', 
            btn_fg='white')
        self.buttons[0].set_display(0, 0)

        self.buttons[0] = SqButton(
            root, self, text='TEXT TO MORSE\n明文轉電碼', 
            btn_fg='white')
        self.buttons[0].set_display(1, 0)

        self.buttons[0] = SqButton(
            root, self, text='MORSE TO TEXT\n電碼轉明文',
            btn_fg='white')
        self.buttons[0].set_display(2, 0)

        self.buttons[0] = SqButton(
            root, self, text='RESET PROGRAM\n刷新程序',
            btn_fg='white')
        self.buttons[0].set_display(3, 0)
    
if __name__ == '__main__': 
    root = tk.Tk() 
    bb = ButtonBar(root)
    bb.grid(column=0, row=0)

    tk.mainloop()