import argparse
import sys 
from motor import ChineseParser as Parser

print(sys.path[0])

"""
Morse to Text 
"""
def morse_to_text(input_string): 
    pass 

if __name__ == '__main__':
    shinter = argparse.ArgumentParser(
                        prog='hanzimorse',
                        description='\
                            Hanzi <- Telegraph Code -> Morse\n\
                            (中文)漢字 <-- 商碼 --> 電報碼',
                        formatter_class=argparse.RawTextHelpFormatter,
                        epilog='A program by K6MLX.\n由K6MLX開發製作.',
                        add_help=False
                        )
    
    shinter.add_argument(
        '-h', 
        '--help', 
        action='help', 
        help='show this help message and exit\n显示本指南后结束程序'
    )

    shinter.add_argument(
        '-v', 
        '--verbose', 
        action='store_true',
        dest='verbose', 
        help='run in verbose mode\n使用話癆模式'
    )

    shinter.add_argument(
        '-l', 
        '--load', 
        action='store',
        nargs=1,
        dest='loadname', 
        help=f'load input from a file path (LOADNAME)\n由文件路徑(LOADNAME)导入'
    )

    shinter.add_argument(
        '-s', 
        '--standard', 
        action='store',
        nargs = 1, 
        metavar='standard', 
        choices=['T', 'S'], 
        default='T',
        help=f'specify a standard to use\n選擇一種字型(T-繁, S-簡)\ndefault: T\n默認使用繁體字 因爲繁體字庫涵蓋範圍更廣'
    )

    shinter.add_argument(
        '-i', 
        '--input', 
        action='store', 
        nargs=1, 
        dest='input_string', 
        help=f'manually feed a string of text (INPUT_STRING)->Morse Code\n手動輸入字符串(INPUT_STRING)->電碼'
    )

    shinter.add_argument(
        '-m', 
        '--morse', 
        action='store', 
        nargs=1, 
        dest='input_morse', 
        help=f'manually feed a string of formatted morse code (INPUT_MORSE)->Text\n手動輸入電碼字符串(INPUT_MORSE)->明文'
    )

    shinter.add_argument(
        '--ready2send', 
        action='store_true', 
        dest='isReady', 
        help=f'use this option if you want the output string formatted for https://morsecode.world/international/translator.html'
    )

    app = shinter.parse_args()
    inputstr = u''
    inputmorse = u''
    # Text -> Morse
    if app.input_string and not app.input_morse: 
        inputstr = app.input_string[0]
        if app.verbose: print(f'T2M Your input: {inputstr}, standard {app.standard}')
        print(f'Output format 輸出格式: a/s/c/i/i/</中/文/數/字/碼/>/')
        result = Parser.text_to_morse(inputstr, standard=app.standard, v_mode=app.verbose)
    # Morse -> Text
    elif app.input_morse and not app.input_string: 
        inputmorse = app.input_morse[0]
        if app.verbose: print(f'M2T Your input: {inputmorse}, standard {app.standard}')
        result = Parser.morse_to_text(inputmorse, standard=app.standard, v_mode=app.verbose, disp_telecode=app.verbose)
    else: 
        shinter.print_help()
        sys.exit(1)
    print(f'Translated string:\n轉譯后的字符串:\n{result}')

    if app.isReady: 
        result = result.replace('/', ' ')
        result = result.replace('_', '/')
        result = result.replace('<', '/')
        result = result.replace('>', '/')
        result = result.replace(' / / ', '/')
        print(f'Ready to Send String:\n{result}')
    
"""
    text = 'hello world! 你好世界! 114514 word'
    morse = Parser.text_to_morse(text, standard='T')
    text = Parser.morse_to_text(morse, v_mode=False, disp_telecode=True)
    print(f'{text} to Morse is \n{morse}')
    print(f'Main: Morse back to text: \n{text}')
"""
