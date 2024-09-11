import tkinter as tk

class StringBox(tk.Frame): 
    def __init__(self, root, width=1200, height=300): 
        tk.Frame.__init__(self, root, width=0, height=0)
        self.frame = tk.Frame(root, width=width, height=height)

        self.tbox = tk.Text(self.frame, width=0, height=0, font=('Noto Sans SemiBold', 20))
        
        self.frame.grid(column=0, row=0)
        self.frame.grid_propagate(False)
        self.frame.columnconfigure(0, weight=1)
        self.frame.rowconfigure(0, weight=1)
        
        self.tbox.grid(column=0, row=0)
        self.tbox.grid(sticky='eswn')
        return None 

    def get_box_input(self): 
        string = self.tbox.get('1.0', 'end-1c')
        return string 

if __name__ == '__main__': 
    root = tk.Tk()
    sb = StringBox(root)
    sb.grid(column=0, row=0)
    tk.mainloop()