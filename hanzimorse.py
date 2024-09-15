import argparse
import sys 

import motor.ChineseParser as Parser
import motor.GuiDriver as Driver

import tkinter as tk

from gui.gui import MainWindow as mw

class ColorHelper: 
    ANSI_RESET = '\033[0m'

    def set_color_by_id(gnd, color_id): 
        outstr = '\033['
        if gnd == 'fg': 
            outstr += f'38;5;{color_id}m'
        elif gnd =='bg': 
            outstr += f'48;5;{color_id}m'
        return outstr

    def set_color_by_rgb(gnd, r, g, b): 
        outstr = '\033['
        if gnd == 'fg': 
            outstr += f'38;2;{r};{g};{b}m'
        elif gnd =='bg': 
            outstr += f'48;2;{r};{g};{b}m'
        return outstr

# color helper instance, 
# easy to pass around 
color = ColorHelper
"""
Morse to Text
"""
# print(f'{color.set_color_by_rgb('fg', 0, 0, 0)}{color.set_color_by_rgb('bg', 255, 121, 0)}  DEV: Current working directory: {sys.path[0]}  {color.ANSI_RESET}')
if __name__ == '__main__':
    shinter = argparse.ArgumentParser(
                        prog='hanzimorse',
                        description=f'\
                            {color.set_color_by_rgb('fg', 0, 255, 173)}Hanzi <- Telegraph Code -> Morse\n\
                            (中文)漢字 <-- 商碼 --> 電報碼{color.ANSI_RESET}',
                        formatter_class=argparse.RawTextHelpFormatter,
                        epilog=f'{color.set_color_by_rgb('fg', 0, 255, 173)}A program by K6MLX.\n由K6MLX開發製作.{color.ANSI_RESET}',
                        add_help=False
                        )
    
    shinter.add_argument(
        '-h', 
        '--help', 
        action='help', 
        help=f'{color.set_color_by_rgb('fg', 255, 255, 0)}show this help message and exit\n显示本指南后结束程序{color.ANSI_RESET}'
    )

    shinter.add_argument(
        '-v', 
        '--verbose', 
        action='store_true',
        dest='verbose', 
        help=f'{color.set_color_by_rgb('fg', 255, 255, 0)}run in verbose mode\n使用話癆模式{color.ANSI_RESET}'
    )

    shinter.add_argument(
        '-l', 
        '--load', 
        action='store',
        nargs=1,
        dest='loadname', 
        help=f'{color.set_color_by_rgb('fg', 255, 255, 0)}load input from a file path (LOADNAME)\n由文件路徑(LOADNAME)导入{color.ANSI_RESET}'
    )

    shinter.add_argument(
        '-s', 
        '--standard', 
        action='store',
        nargs = 1, 
        dest='standard', 
        choices=['T', 'S'], 
        default='T',
        help=f'{color.set_color_by_rgb('fg', 255, 255, 0)}\
            specify a standard to use\n\
            選擇一種字型(T-繁, S-簡)\n\
            default: T\n\
            默認使用繁體字 因爲繁體字庫涵蓋範圍更廣{color.ANSI_RESET}'
    )

    shinter.add_argument(
        '-i', 
        '--input', 
        action='store', 
        nargs=1, 
        dest='input_string', 
        help=f'{color.set_color_by_rgb('fg', 255, 255, 0)}\
            manually feed a string of text (INPUT_STRING)->Morse Code\n\
            手動輸入字符串(INPUT_STRING)->電碼{color.ANSI_RESET}'
    )

    shinter.add_argument(
        '-m', 
        '--morse', 
        action='store', 
        nargs=1, 
        dest='input_morse', 
        help=f'{color.set_color_by_rgb('fg', 255, 255, 0)}\
            manually feed a string of formatted morse code (INPUT_MORSE)->Text\n\
            手動輸入電碼字符串(INPUT_MORSE)->明文{color.ANSI_RESET}'
    )

    shinter.add_argument(
        '--ready2send', 
        action='store_true', 
        dest='isReady', 
        help=f'{color.set_color_by_rgb('fg', 255, 255, 0)}\
            use this option if you want the output string formatted for {color.ANSI_RESET}\n\
            {color.set_color_by_rgb('fg', 0, 255, 255)}https://morsecode.world/international/translator.html{color.ANSI_RESET}'
    )
    
    shinter.add_argument(
        '-g', 
        '--gui', 
        action='store_true', 
        dest='use_gui', 
        help=f'{color.set_color_by_rgb('fg', 255, 255, 0)}\
            (Dev) Use GUI{color.ANSI_RESET}\n'
    )

    app = shinter.parse_args()
    inputstr = u''
    inputmorse = u''

    if app.use_gui: 
        root = tk.Tk()
        MainWindow = mw(root,gui_cmds=Driver.get_cmds())
        MainWindow.place(x=2,y=2)
        root.geometry('1204x704')
        root.title('Chinese Morse Tool')
        root.mainloop()

    # Text -> Morse
    if app.input_string and not app.input_morse: 
        inputstr = app.input_string[0]
        if app.verbose: print(f'T2M Your input: {inputstr}, standard {app.standard[0]}')
        result = Parser.text_to_morse(inputstr, standard=app.standard[0], v_mode=app.verbose)
        f_result = result 
        f_result = f_result.replace('\uFFFD', '')
        f_result = f_result.replace(' } ', ' }')
        print(f'Translated string:\n轉譯后的字符串:\n{color.ANSI_RESET}\033[1m{color.set_color_by_rgb('bg', 255, 121, 0)}{color.set_color_by_rgb('fg', 0, 0, 0)}\'{f_result}\'{color.ANSI_RESET}')
        verified = False 
        v_result = Parser.morse_to_text(f_result, v_mode=app.verbose)
        print(f'Morse back to text: {v_result}')

    # Morse -> Text
    elif app.input_morse and not app.input_string: 
        inputmorse = app.input_morse[0]
        if app.verbose: print(f'M2T Your input: {inputmorse}, standard {app.standard[0]}')
        result = Parser.morse_to_text(inputmorse, standard=app.standard[0], v_mode=app.verbose, disp_telecode=app.verbose)
        print(f'Translated string:\n轉譯后的字符串:\n{color.ANSI_RESET}\033[1m{color.set_color_by_rgb('bg', 255, 121, 0)}{color.set_color_by_rgb('fg', 0, 0, 0)}\'{result}\'{color.ANSI_RESET}')

    else: 
        shinter.print_help()
        sys.exit(1)

    if app.isReady: 
        result = result.replace(u'\uFFFD', '')
        result = result.replace(' { ', '')
        result = result.replace(' } ', '')
        print(f'Ready to Send String:\n{color.ANSI_RESET}\033[1m{color.set_color_by_rgb('bg', 255, 121, 0)}{color.set_color_by_rgb('fg', 0, 0, 0)}\'{result}\'{color.ANSI_RESET}')

