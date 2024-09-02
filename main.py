import argparse
import sys 
from motor import ChineseParser as Parser

if __name__ == '__main__':
    print("Chinese Morse Tool")
    text = 'hello world! 你好世界! 114514 word'
    morse = Parser.text_to_morse(text, standard='T')
    text = Parser.morse_to_text(morse, v_mode=False)
    print(f'{text} to Morse is \n{morse}')
    print(f'Main: Morse back to text: \n{text}')