text = "IYHCV CVBZ HCLG JHZZL SL JOPMMYL KL JLZHY"
text = text.lower()
def decrypt_cesar(text):

    for decalage in range(25) : 
        message = ""

        for i in text :
            if i ==" " :
                message += " "
                continue
             
            i= ord(i)-decalage
            if i < 97 : 
                i +=26
            message += chr(i)
        print(decalage," : ",message,"\n")

decrypt_cesar(text)