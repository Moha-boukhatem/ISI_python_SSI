import numpy as np
text="abc"
decalage = 1

############################# crypt/decrypt Cesar ##################################

def crypt_cesar(text,decalage):
    message = ""
    for i in text :
        i= ord(i)+decalage
        message += chr(i)
    return message

def decrypt_cesar(text,decalage):
    message = ""
    for i in text :
        i= ord(i)-decalage
        message += chr(i)
    return message

print(crypt_cesar(text,decalage))
print(decrypt_cesar(text,decalage))




