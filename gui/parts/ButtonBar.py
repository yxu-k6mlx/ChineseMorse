import tkinter as tk
from gui.parts.SqButton import SqButton as SqButton

class ButtonBar(tk.Frame): 
    def __init__(self, root, width=1200, height=100, btncmds=[None]*4): 
        tk.Frame.__init__(self, root, width=width, height=height) 

        self.buttons = [None]*4
        self.cmds = btncmds
        
        self.buttons[0] = SqButton(
            root, self, text='LOAD INPUT\n載入文字', 
            btn_fg='white', width=300)

        self.buttons[1] = SqButton(
            root, self, text='TEXT TO MORSE\n明文轉電碼', 
            btn_fg='white', width=300)

        self.buttons[2] = SqButton(
            root, self, text='MORSE TO TEXT\n電碼轉明文',
            btn_fg='white', width=300)

        self.buttons[3] = SqButton(
            root, self, text='RESET PROGRAM\n刷新程序',
            btn_fg='white', width=300)
        
        for i in range (0, len(self.buttons)): 
            self.buttons[i].set_cmd(self.cmds[i])
            self.buttons[i].set_display(i, 0)
         
if __name__ == '__main__': 
    root = tk.Tk() 
    bb = ButtonBar(root)
    bb.grid(column=0, row=0)

    tk.mainloop()