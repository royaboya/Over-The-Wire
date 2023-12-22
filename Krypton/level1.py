
"""
Prompt:
The password for level 2 is in the file ‘krypton2’. It is ‘encrypted’ using a simple rotation. It is also in non-standard ciphertext format. When using alpha characters for cipher text it is normal to group the letters into 5 letter clusters, regardless of word boundaries. This helps obfuscate any patterns.
 This file has kept the plain text word boundaries and carried them to the cipher text. Enjoy!

CyberChef rot13: "YRIRY GJB CNFFJBEQ EBGGRA" -> "LEVEL TWO PASSWORD ROTTEN" 

or python
"""

# File contents: YRIRY GJB CNFFJBEQ EBGGRA

def decoderot13(plain_text:str, offset=13) -> str:
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    letter_to_numbers = {alphabet[i]:i for i in range(len(alphabet))}
    decoded = ""


    for letter in plain_text:
        if letter.isalpha():
            decoded += alphabet[(letter_to_numbers[letter] + offset) % len(alphabet)]
        else:
            decoded += letter    

    print(decoded)



decoderot13("YRIRY GJB CNFFJBEQ EBGGRA", 13)