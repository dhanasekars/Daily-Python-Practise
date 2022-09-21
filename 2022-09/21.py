""" 
Created on : 21/09/22 5:32 AM
@author : ds  
"""


test_data = "HELP ME !%"


def encode_morse(sos):
    sos = sos.upper()
    sos = sos.replace("", " ")[1:-1]
    char_to_dots = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
        'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
        'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
        'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..', ' ': ' ', '0': '-----',
        '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.',
        '&': '.-...', "'": '.----.', '@': '.--.-.', ')': '-.--.-', '(': '-.--.',
        ':': '---...', ',': '--..--', '=': '-...-', '!': '-.-.--', '.': '.-.-.-',
        '-': '-....-', '+': '.-.-.', '"': '.-..-.', '?': '..--..', '/': '-..-.'
    }
    morse = ""
    for c in sos:
        try :
            morse = morse + char_to_dots[c]
        except KeyError:
            morse = morse + '#'
    return morse

# pythonic --> return ' '.join(chars_to_dots[c] for c in sos.upper())
# The above did not factor in keyerror.


print(encode_morse(test_data))