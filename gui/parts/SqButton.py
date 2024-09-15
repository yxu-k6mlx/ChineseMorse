import tkinter as tk 

class SqButton(tk.Frame): 
    def __init__(
        self, root, frame, width=150, height=100, text='Default\nTest', 
        btn_fg='#000000', btn_bg='#006747', active_btn_fg='#f0f0f0', active_btn_bg='#da291c'): 
        tk.Frame.__init__(self, root, width=width, height=height) 
        
        self.btn_frame = frame

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
        
        return None
    
    def set_display(self, col, row): 
        self.btn_frame.grid(column=0, row=0)
        self.btn_frame.grid_propagate(False)
        self.btn_frame.rowconfigure(row, weight=1)
        self.btn_frame.columnconfigure(col, weight=1)

        self.btn.grid(column=col, row=row)
        self.btn.grid(sticky='eswn')
        return True
    
    def set_cmd(self, cmd): 
        self.btn.configure(command=cmd)
        return True

