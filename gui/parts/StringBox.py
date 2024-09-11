import tkinter as tk

class StringBox(tk.Frame): 
    def __init__(self, root, width=1200, height=300): 
        tk.Frame.__init__(self, root, width=0, height=0) 
        self.tbox = tk.Text(root, width=int(width/10), height=int(height/10))
        self.tbox.grid(column=0, row=0)
        
        return None 

    def get_box_input(self): 
        string = self.tbox.get('1.0', 'end-1c')
        return string 

if __name__ == '__main__': 
    root = tk.Tk()
    sb = StringBox(root)
    sb.grid(column=0, row=0)
    tk.mainloop()