import tkinter as tk
from ChineseMorse.gui.parts.ControlButton import SqButton

class ButtonBar(tk.Frame): 
    def __init__(self, root, width=1600, height=100): 
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

        for i in range(0, 8): 
            self.sq_btn = SqButton(root, self, text=self.text_labels[i])
            print(f'i={i}; txt={self.text_labels[i]}')
            self.sq_btn.set_display(i, 0)

        return None 
    
if __name__ == '__main__': 
    root = tk.Tk() 
    bb = ButtonBar(root)
    bb.grid(column=0, row=0)

    tk.mainloop()