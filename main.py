import argparse
import sys 
from motor import ChineseParser as Parser

if __name__ == '__main__':
    print("Chinese Morse Tool")
    morse = Parser.text_to_morse('hello world! 你好世界! ', standard='T')
    text = Parser.morse_to_text(Parser.text_to_morse('hello world! 你好世界! ', standard='T', v_mode=True), v_mode=True)
    print(f'Main: Hello world! 你好世界! \n{morse}')
    print(f'Main: Morse back to text: \n{text}')