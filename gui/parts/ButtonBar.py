import tkinter as tk
from parts.SqButton import SqButton

class ButtonBar(tk.Frame): 
    def __init__(self, root, width=1200, height=100): 
        tk.Frame.__init__(self, root, width=width, height=height) 

        self.text_labels = [
            'Button\n1',
            'Button\n2', 
            'Button\n3', 
            'Button\n4', 
            'Button\n5', 
            'Button\n6', 
            'Button\n7', 
            'Button\n8'
        ]

        self.buttons = [None]*8

        for i in range(0, 8): 
            self.btn = SqButton(root, self, text=self.text_labels[i])
            self.buttons[i] = self.btn.get_self()
            self.buttons[i].set_display(i, 0)
            self.btn = None 
        return None 
    
if __name__ == '__main__': 
    root = tk.Tk() 
    bb = ButtonBar(root)
    bb.grid(column=0, row=0)

    tk.mainloop()