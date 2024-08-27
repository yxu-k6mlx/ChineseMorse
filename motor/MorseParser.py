import MorseDict as Lookup
import codecs
import math

def latin_to_morse(input_string, add_slash=True) -> str: 
    output_string = ''
    for char in input_string: 
        output_string = output_string + Lookup.latin_to_morse(char, add_break=add_slash)

    return output_string

def morse_to_latin(input_morse, add_slash=False) -> str:
    #print(f'add slash={add_slash}')
    output_string = ''
    codes = []
    read_head = 0
    last_slash = 0

    for char in input_morse: 
        if char == '/': 
            codes.append(input_morse[last_slash:read_head])
            
            read_head += 1
            last_slash = read_head
        else: 
            read_head += 1
    
    #print(codes)
    
    num_counter = 0
    for code in codes: 
        #print(f'counter={num_counter}')
        holder = Lookup.morse_to_latin(code)
        
        if holder is not None: 
            output_string += holder 
        else: 
            output_string += ''
    
    return output_string
