import csv 
import io
import MorseParser as Parser

def char_to_num(letter, standard) -> str:
    counter=0 
    #print(f'Char: {letter}, std: {standard}')
    if standard == 'T': 
        # traditional standard
        raw_file = io.open(r'ChineseMorse\csv\twtelegraph.csv', mode='r') 
        trad_codes = csv.reader(raw_file)
        for raw_char, code in trad_codes: 
            #print(f'counter={counter},raw_char={raw_char},code={code}')
            char = bytes(raw_char, "ascii").decode("unicode-escape")
            #print(f'decoded = {char}')
            if letter == char: 
                print(f'Match found for {letter} at {code}')
                return code
        return None
            
    elif standard == 'S': 
        # mainlander standard
        raw_file = io.open(r'ChineseMorse\csv\cntelegraph.csv', mode='r') 
        simp_codes = csv.reader(raw_file)
        for raw_char, code in simp_codes: 
            #print(f'counter={counter},raw_char={raw_char},code={code}')
            char = bytes(raw_char, "ascii").decode("unicode-escape")
            #print(f'decoded = {char}')
            if letter == char: 
                print(f'Match found for {letter} at {code}')
                return code
        return None
    
def text_to_morse(in_string, standard): 
    out_str = ''
    counter = 0
    for element in in_string: 
        code = char_to_num(element, standard)
        if code is not None: 
            # is hanzi
            out_str += '{' + Parser.latin_to_morse(code, add_slash=True) + '}'
        else: 
            # is alpha numeric
            code = Parser.latin_to_morse(element, add_slash=True)
            out_str += code
    print(f'Your morse is {out_str}')
    counter = 0
    return out_str

def morse_to_text(in_string, standard): 
    raw_string = Parser.morse_to_latin(in_string, add_slash=True)
    print(raw_string)

morse_to_text(text_to_morse('hello world! 你好世界! ', standard='T'), standard='T')