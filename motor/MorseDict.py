
# src https://www.itu.int/dms_pubrec/itu-r/rec/m/R-REC-M.1677-1-200910-I!!PDF-E.pdf
itu_morse = [
    # Char
    ('A', '.-'), 
    ('B', '-...'), 
    ('C', '-.-.'),
    ('D', '-..'), 
    ('E', '.'), 
    ('F', '..-.'), 
    ('G', '--.'),
    ('H', '....'), 
    ('I', '..'), 
    ('J', '.---'), 
    ('K', '-.-'), 
    ('L', '.-..'), 
    ('M', '--'), 
    ('N', '-.'), 
    ('O', '---'), 
    ('P', '.--.'), 
    ('Q', '--.-'), 
    ('R', '.-.'), 
    ('S', '...'), 
    ('T', '-'), 
    ('U', '..-'), 
    ('V', '...-'), 
    ('W', '.--'), 
    ('X', '-..-'), 
    ('Y', '-.--'), 
    ('Z', '--..'),
    # Num
    ('0', '-----'), 
    ('1', '.----'), 
    ('2', '..---'),
    ('3', '...--'), 
    ('4', '....-'), 
    ('5', '.....'), 
    ('6', '-....'), 
    ('7', '--...'), 
    ('8', '---..'), 
    ('9', '----.'), 
    # Punc
    ('.', '.-.-.-'), # Period
    (',', '--..--'), # Comma
    (':', '---...'), # Colon
    ('?', '..--..'), # Question
    ('\'', '.----.'), # Apostrophe 
    ('-', '-....-'), 
    ('/', '-..-.'), 
    ('(', '-.--.'), 
    (')', '-.--.-'), 
    ('\"', '.-..-.'), # Quote
    ('=', '-...-'), 
    ('+', '.-.-.'), 
    ('*', '-..-'), # Multiply (X)
    ('@', '.--.-.'),
    # Specials
    ('<UNDERSTAND>', '..-.'), # Understand
    ('<ERROR>', '........'), 
    ('<INVITE>', '-.-'), 
    ('<WAIT>', '.-...'), 
    ('<SIGNOUT>', '...-.-'), 
    ('<EOM>', '.-.-.'), 
    ('<START>', '-.-.-'), 
    # Space
    (' ', '_'), 
    # Non-ITU but acceptable
    ('!', '-.-.--')
]

itu_pace = [
    ('<SIG_BREAK>', '/'), 
    ('<CHAR_BREAK>', '///'), 
    ('<WORD_BREAK>', '///////'), 
]

"""
Transforms a latin char to morse in string
Letter breaks are added by default

Params: 
    string char - A single character or special code to be translated
    bool add_break - option to add '/' between letters
Returns: morse
"""
def latin_to_morse(char, add_break=True) -> str: 
    char = char.capitalize() 
    for latin, morse in itu_morse: 
        if latin == char: 
            if add_break: 
                return f'{morse}/'
            else: 
                return f'{morse}'

"""
Transforms a single character or special code in morse to letter
No spaces are inserted here
"""
def morse_to_latin(morse, add_space=False) -> str: 
    for latin, target in itu_morse: 
        if morse == target: 
            if add_space: 
                return f'{latin} '
            else: 
                return latin
            
