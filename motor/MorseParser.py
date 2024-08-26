import MorseDict as Lookup

def latin_to_morse(input_string, add_slash=True) -> str: 
    output_string = ''
    for char in input_string: 
        if add_slash: 
            output_string = output_string + str(Lookup.latin_to_morse(char, add_break=add_slash))
        else: 
            output_string = output_string + Lookup.latin_to_morse(char) + ' '

    return output_string

def morse_to_latin(input_morse) -> str:
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
    
    for code in codes: 
        output_string += Lookup.morse_to_latin(code)
    
    return output_string
