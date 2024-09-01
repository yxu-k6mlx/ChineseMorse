import tkinter as tk

class Square(tk.Frame): 
    def __init__(
            self, 
            root, 
            text='', 
            type='warn', 
            digit=0
        ) -> None: 

        self.tk = root 
        self.digit = digit 
        self.text = text 
        self._w = tk.Button(
            root, 
            width=5, height=5, 
            text=text, 
            borderwidth=1, 
            highlightthickness=0, 
            justify='center', 
            padx=0, 
            pady=0, 
            relief='solid'
        )

        if (type == 'warn'): 
            self._w.config()
        elif (type == 'error'): 
            self._w.config()
        elif (type == 'digit_display'): 
            pass 
        elif (type == 'text_display'): 
            pass 
        elif (type == 'toggle'): 
            pass 
        elif (type == 'simple'): 
            pass 
        else: 
            return None

    def set_digit(self, digit): 
        pass

    def get_digit(self): 
        pass

    def set_text(self, text): 
        pass

    def get_text(self): 
        pass

if __name__ == '__main__': 
    test = tk.Tk()
    square = Square(test)
    #square.button.grid(column=0, row=0)
    for j in range(0, 2): 
        for i in range(0, 8): 
            string = f'({i},{j})'
            new_button = Square(test, text=string)
            print(string)
            new_button.grid(column=i, row=j)
    tk.mainloop()