import base64

"""
Prompt:

Welcome to Krypton! The first level is easy. The following string encodes the password using Base64:

S1JZUFRPTklTR1JFQVQ=

Use this password to log in to krypton.labs.overthewire.org with username krypton1 using SSH on port 2231. You can find the files for other levels in /krypton/
"""
to_decode = base64.b64decode("S1JZUFRPTklTR1JFQVQ=")

print(to_decode) # b'KRYPTONISGREAT'
