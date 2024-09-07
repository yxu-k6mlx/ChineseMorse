import csv 
import io
import motor.MorseParser as Parser
import platform

def char_to_num(letter, standard, v_mode=False) -> str:
    #counter=0 
    #print(f'Char: {letter}, std: {standard}')
    if standard == 'T': 
        # traditional standard
        if platform.system == 'Windows': 
            raw_file = io.open(r'ChineseMorse\csv\twtelegraph.csv', mode='r') 
        else:
            raw_file = io.open('ChineseMorse/csv/twtelegraph.csv', mode='r')
        trad_codes = csv.reader(raw_file)
        for raw_char, code in trad_codes: 
            char = bytes(raw_char, "ascii").decode('unicode-escape')
            if letter == char: 
                if v_mode: print(f'CP-C2N/T: Match found for {letter} at {code}')
                code = '<' + code +'>'
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
            char = bytes(raw_char, "ascii").decode('unicode-escape')
            if letter == char: 
                if v_mode: print(f'CP-C2N/S: Match found for {letter} at {code}')
                code = '<' + code +'>'
                return code
        return None
    
def text_to_morse(in_string, standard, v_mode=False): 
    out_str = ''
    
    for element in in_string: 
        # try to find a match 
        code = char_to_num(element, standard, v_mode=v_mode)
        if code is None: 
            if v_mode: print(f'CP-T2M: Tried to match {element} to {code}, but no code found! ')
            # no codes found on hanzi dict
            if element: 
                # is alpha-numeric 
                # get classic morse
                if v_mode: print(f'CP-T2M: {element} is ASCII, send to Latin2Morse direct. ')
                out_str += Parser.latin_to_morse(element, add_slash=True, v_mode=v_mode)
            else: # is not alnum and no code found 
                # try and see if the other standard covered this hanzi
                if standard == 'T': 
                    trycode = char_to_num(element, standard='S', v_mode=v_mode)
                    if v_mode: print(f'CP-T2M: Found {element} - {trycode} in Traditional Hanzi Dict')
                elif standard == 'S': 
                    trycode = char_to_num(element, standard='T', v_mode=v_mode)
                    if v_mode: print(f'CP:T2M: Found {element} - {trycode} in Simplified Hanzi Dict')
                # if covered, add to out_str
                if trycode is not None: 
                    out_str += trycode 
        else:  
            # is hanzi with code
            if v_mode: print(f'CP-T2M: Matched {element} to {code}')
            out_str += Parser.latin_to_morse(code, add_slash=True, v_mode=v_mode)
    if v_mode: print(f'CP-T2M: Your morse is {out_str}')
    
    return out_str

def num_to_char(nums, standard='T', v_mode=False): 
    codeword = ''
    hanzi = ''
    for char in nums: 
        if char.isnumeric: 
            codeword += char
    if standard == 'T': 
        if platform.system == 'Windows': 
            raw_file = io.open(r'ChineseMorse\csv\twtelegraph.csv', mode='r') 
        else:
            raw_file = io.open('ChineseMorse/csv/twtelegraph.csv', mode='r')
    elif standard == 'S': 
        if platform.system == 'Windows': 
            raw_file = io.open(r'ChineseMorse\csv\cntelegraph.csv', mode='r') 
        else:
            raw_file = io.open('ChineseMorse/csv/cntelegraph.csv', mode='r')
    else: print('CP-N2C/?: Standard Undefined') 
    codes = csv.reader(raw_file)
    for char, code in codes: 
        if code == codeword: 
            if v_mode: print(f'CP-N2C: {codeword} matched with {char}')
            hanzi += char

    return hanzi

def morse_to_text(in_string, standard='T', v_mode=False, disp_telecode=False): 
    raw_string = Parser.morse_to_latin(in_string, has_brackets=True, v_mode=v_mode)
    if v_mode: print(f'CP-M2T: {raw_string}')
    left_limit = 0
    current_index = 0
    hanzi_num = ''
    text = ''
    is_hanzi = False
    hanzi_codes = ''
    for char in raw_string: 
        if v_mode: print(f'CP-M2T: char = {char}')
        
        if char == '<' and raw_string[current_index+1].isnumeric: 
            if v_mode: print(f'CP-M2T: Found \'<\' at {current_index}')
            left_limit = current_index + 1
            current_index += 1
            is_hanzi = True
        elif char == '>': 
            if v_mode: print(f'CP-M2T: Found \'>\' at {current_index}')
            hanzi_num += (raw_string[left_limit:current_index])
            if v_mode: print(f'CP-M2T: Hanzi Num is {hanzi_num}, sent to num2char')
            unicode_holder = num_to_char(hanzi_num, standard=standard, v_mode=v_mode)
            if v_mode: print(f'CP-M2T: Unicode = {unicode_holder}')
            text += unicode_holder
            if v_mode: print(f'CP-M2T: text = {text}')

            hanzi_codes += unicode_holder + ' - <' + hanzi_num + '>\n'
            hanzi_num = ''
            left_limit = 0
            current_index += 1
            is_hanzi = False
        else:
            if v_mode: print(f'CP-M2T: else: char = {char}')
            if not is_hanzi: text += char
            current_index += 1

    text = bytes(text, "ascii").decode('unicode-escape')
    if v_mode: 
        print(f'CP-M2T: Text found: {text}')
    if disp_telecode: 
        hanzi_codes = bytes(hanzi_codes, 'ascii').decode('unicode-escape')
        print(f'All Hanzi found and their telecodes: ')
        print(hanzi_codes)
    return text

#morse_to_text(text_to_morse('hello world! 你好世界! ', standard='T'), standard='T')