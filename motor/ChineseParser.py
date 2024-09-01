import csv 
import io
import motor.MorseParser as Parser
import platform

def char_to_num(letter, standard, v_mode=False) -> str:
    counter=0 
    #print(f'Char: {letter}, std: {standard}')
    if standard == 'T': 
        # traditional standard
        if platform.system == 'Windows': 
            raw_file = io.open(r'ChineseMorse\csv\twtelegraph.csv', mode='r') 
        else:
            raw_file = io.open('ChineseMorse/csv/twtelegraph.csv', mode='r')
        trad_codes = csv.reader(raw_file)
        for raw_char, code in trad_codes: 
            char = bytes(raw_char, "ascii").decode("unicode-escape")
            if letter == char: 
                if v_mode: print(f'CP-C2N/T: Match found for {letter} at {code}')
                #code = '<' + code +'>'
                return code
        return None
            
    elif standard == 'S': 
        # mainlander standard
        if platform.system == 'Windows': 
            raw_file = io.open(r'ChineseMorse\csv\cntelegraph.csv', mode='r') 
        else: 
            raw_file = io.open('ChineseMorse/csv/cntelegraph.csv', mode='r')
        simp_codes = csv.reader(raw_file)
        for raw_char, code in simp_codes: 
            char = bytes(raw_char, "ascii").decode("unicode-escape")
            if letter == char: 
                if v_mode: print(f'CP-C2N/S: Match found for {letter} at {code}')
                #code = '<' + code +'>'
                return code
        return None
    
def text_to_morse(in_string, standard, v_mode=False): 
    out_str = ''
    
    for element in in_string: 
        code = char_to_num(element, standard, v_mode=v_mode)
        if code is not None: 
            # is hanzi
            out_str += Parser.latin_to_morse(code, add_slash=True, v_mode=v_mode)
        else: 
            # is alpha numeric
            code = Parser.latin_to_morse(element, add_slash=True, v_mode=v_mode)
            out_str += code
    if v_mode: print(f'CP-T2M: Your morse is {out_str}')
    
    return out_str

def morse_to_text(in_string, v_mode=False): 
    raw_string = Parser.morse_to_latin(in_string, has_brackets=True, v_mode=v_mode)
    if v_mode: print(f'CP-M2T: {raw_string}')
    return raw_string

#morse_to_text(text_to_morse('hello world! 你好世界! ', standard='T'), standard='T')