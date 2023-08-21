morse_code_dict = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.',
    'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.',
    'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-',
    'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--', 'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.',
    ' ': ' '  # from online you will get  
}


# this is main block of your code where you will take each char from string 
# and compare from dict and if you will find
# char from dict you will append that morse code to new created list 
  
def morse_conversion(string):           # function define 
    morse_code = []                         # new list 
    for char in string.upper():
        if char in morse_code_dict:
            morse_code.append(morse_code_dict[char])             # access the morse code from dictionary
        else:
            morse_code.append('') 
    return ' '.join(morse_code)

input_string = input("Enter a string :  ")           #take input from user 
morse_result = morse_conversion(input_string)       # here we will call our function (morse_conversion)
print("Morse code:", morse_result)                    # print our result 