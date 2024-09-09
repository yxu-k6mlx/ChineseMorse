import motor.MorseDict as Lookup

def latin_to_morse(input_string, add_slash=True, v_mode=False) -> str: 
    if v_mode: print(f'MP-L2M: Received \'{input_string}\'')
    output_string = ''
    for char in input_string: 
        output_string = output_string + Lookup.latin_to_morse(char, add_break=False) + '/'
    if v_mode: print(f'MP-L2M: Morse found \'{output_string}\'')
    return output_string

def morse_to_latin(input_morse, has_brackets=False, v_mode=False) -> str:
    output_string = ''
    codes = []
    read_head = 0
    last_slash = 0
    if v_mode: print(f'MP-M2L: {input_morse}')
    
    for char in input_morse: 
        if v_mode: print(f'MP-M2L: char: {char}')
        if char == '/': 
            codes.append(input_morse[last_slash:read_head])
            
            read_head += 1
            last_slash = read_head
            
        else: 
            read_head += 1
    
    if v_mode: print(f'MP-M2L: Codes: {codes}')
    
    for code in codes: 
        #print(f'counter={num_counter}')
        holder = Lookup.morse_to_latin(code)
        
        if holder is not None: 
            output_string += holder
        else: 
            output_string += ''
    
    return output_string
