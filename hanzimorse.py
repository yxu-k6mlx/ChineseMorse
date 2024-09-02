import argparse
import sys 
from motor import ChineseParser as Parse

print(sys.path[0])

def set_verbose(foobar): 
    print(f'\n\nVerbose ON {foobar}')
    pass

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
        help=f'load input from a file\n由文件导入'
    )

    shinter.add_argument(
        '-s', 
        '--standard', 
        action='store',
        nargs = 1, 
        dest='standard', 
        default='T',
        help=f'specify a standard to use\n選擇一種字型\nuse \'T\' for Traditional Chinese\n輸入\'T\'使用繁體字\nuse \'S\' for Simplified Chinese\n輸入\'S\'使用簡體字\ndefault: T\n默認使用繁體字'
    )

    shinter.add_argument(
        '-d', 
        '--dir', 
        dest='dir'
    )

    shinter.print_help()
    app = shinter.parse_args()
    
"""
    text = 'hello world! 你好世界! 114514 word'
    morse = Parser.text_to_morse(text, standard='T')
    text = Parser.morse_to_text(morse, v_mode=False, disp_telecode=True)
    print(f'{text} to Morse is \n{morse}')
    print(f'Main: Morse back to text: \n{text}')
"""
