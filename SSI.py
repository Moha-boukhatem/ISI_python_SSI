text="a"
decalage = 1
def crypt_cesar(text,decalage):
    message = ""
    for i in text :
        i= ord(i)+decalage
        message += chr(i)
    print(message)

crypt_cesar(text,decalage)