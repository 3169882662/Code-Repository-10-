def morse_translator(text):
    # Morse code mapping
    morse_code_dict = {
        "A": ".-", "B": "-...", "C": "-.-.", "D": "-..", "E": ".",
        "F": "..-.", "G": "--.", "H": "....", "I": "..", "J": ".---",
        "K": "-.-", "L": ".-..", "M": "--", "N": "-.", "O": "---",
        "P": ".--.", "Q": "--.-", "R": ".-.", "S": "...", "T": "-",
        "U": "..-", "V": "...-", "W": ".--", "X": "-..-", "Y": "-.--",
        "Z": "--.."
    }
    
    # Convert the text to uppercase to make the function case-insensitive
    text = text.upper()
    
    # Translate each character to Morse code
    morse_code = ''
    for char in text:
        if char in morse_code_dict:
            morse_code += morse_code_dict[char] + ' '
        elif char == ' ':
            morse_code += '/ '
    
    return morse_code.strip()

# Test cases
print(morse_translator("HELLO WORLD"))  # Expected output: ".... . .-.. .-.. --- / .-- --- .-. .-.. -.."
print(morse_translator("Python"))       # Expected output: ".--. -.-- - .... --- -."
print(morse_translator("Morse Code"))   # Expected output: "-- --- .-. ... . / -.-. --- -.. ."
