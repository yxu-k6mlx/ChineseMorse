import csv 
import io
import MorseParser as LatinParser

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
    
def hanzi_parser(in_string, standard): 
    out_str = ''
    for element in in_string: 
        code = char_to_num(element, standard)
        if code is not None: 
            out_str += LatinParser.latin_to_morse(code, add_slash=True) + '/'
        else: 
            code = LatinParser.latin_to_morse(element, add_slash=True)
            if code is not None: 
                out_str += code 

    return out_str
