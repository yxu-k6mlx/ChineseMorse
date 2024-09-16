import motor.ChineseParser as Parser

def get_cmds(): 
    cmds = [None]*4
    cmds[0] = print_text
    cmds[1] = set_gui_output
    return cmds 

def print_text(terminal_string): 
    print(terminal_string)

def set_gui_output(gui_string): 
    pass 
