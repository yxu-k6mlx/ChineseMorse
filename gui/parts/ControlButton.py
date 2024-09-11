import tkinter as tk 

class SqButton(tk.Frame): 
    def __init__(
        self, root, width=180, height=80, text='Default\nTest', 
        btn_fg='#f0f0f0', btn_bg='#006747', active_btn_fg='#f0f0f0', active_btn_bg='#da291c'): 
        tk.Frame.__init__(self, root, width=width, height=height) 
        self.btn_frame = tk.Frame(self, width=width, height=height, bg='white')
        self.btn_frame.grid(column=0, row=0)
        self.btn_frame.grid_propagate(False)
        self.btn_frame.rowconfigure(0, weight=1)
        self.btn_frame.columnconfigure(0, weight=1)

        self.btn = tk.Button(
            self.btn_frame, 

            foreground=btn_fg, 
            background=btn_bg, 
            activeforeground=active_btn_fg, 
            activebackground=active_btn_bg, 

            relief='groove', 
            text=text, 
            font=('Noto Sans SemiBold', 20)
        )
        self.btn.grid(column=0, row=0)
        self.btn.grid(sticky='eswn')
        return None 
    
if __name__ == '__main__': 
    root = tk.Tk()
    button = SqButton(root)
    button.grid(column=0, row=0)
    tk.mainloop()