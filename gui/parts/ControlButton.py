import tkinter as tk 

class SqButton(tk.Frame): 
    def __init__(self, root, width=80, height=60, active='red', inactive='grey'): 
        tk.Frame.__init__(self, root, width=width, height=height, background='blue', highlightthickness=0) 
        self.button = tk.Button(root, foreground='black', text='TEST', justify='center', relief='raised')
        self.button.grid(column=0, row=0)
        return None 
    
if __name__ == '__main__': 
    root = tk.Tk()
    button = SqButton(root)
    button.grid(column=0, row=0)
    tk.mainloop()