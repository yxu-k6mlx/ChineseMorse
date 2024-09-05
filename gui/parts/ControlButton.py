import tkinter as tk 

class SqButton(tk.Frame): 
    def __init__(self, root, width=20, height=5, text='BUTTON TEXT'): 
        self.frame = tk.Frame.__init__(self, root, width=width, height=height, background='purple')
        
        self.width = width 
        self.height = height 

        self.tk_button = tk.Button(
            self.frame, 
            background='#3c3c3c', 
            activebackground='red', 
            justify='center', 

            width=self.width, 
            height=self.height, 
            relief='flat'
        )

        self.tk_label = tk.Label(
            self.frame, 
            foreground='white', 
            background='#3c3c3c', 
            text='SAMPLE\nTEXT', 
            font=('Noto Sans SemiBold', 20), 
            padx=0, 
            pady=0
        )

        self.tk_label.grid(column=0, row=0)
        return None

if __name__ == '__main__': 
    print(f'CtrlButton Main:')
    root = tk.Tk()

    button = SqButton(root)
    button.tk_button.place(x=0, y=0)
    tk.mainloop()