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
                        formatter_class=argparse.RawDescriptionHelpFormatter,
                        epilog='A program by K6MLX.\n由K6MLX開發製作.')
    
    shinter.add_argument(
        '-v', 
        '--verbose', 
        action='store_true',
        dest='verbose', 
        help='Run HanziMorse in verbose mode. 使用話癆模式.'
    )

    shinter.add_argument(
        '-l', 
        '--load', 
        dest='load_file'
    )

    shinter.add_argument(
        '-s', 
        '--standard', 
        dest='standard'
    )

    shinter.add_argument(
        '-d', 
        '--dir', 
        dest='dir'
    )

    shinter.print_help()
    app = shinter.parse_args(['-l test'])

    print(app.load_file[1:])
    
"""
    text = 'hello world! 你好世界! 114514 word'
    morse = Parser.text_to_morse(text, standard='T')
    text = Parser.morse_to_text(morse, v_mode=False, disp_telecode=True)
    print(f'{text} to Morse is \n{morse}')
    print(f'Main: Morse back to text: \n{text}')
"""
