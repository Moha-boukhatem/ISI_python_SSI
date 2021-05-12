import numpy as np


def crypte_polybe() :
    carree  = np.array([["a","b","c","d","e"],
                        ["f","g","h","i","j"],
                        ["k","l","m","n","o"],
                        ["p","q","r","s","t"],
                        ["u","v","x","y","z"]])

    texte1 ="Lhomme est un ange wechu qui se souvient du ciel"
    texte = texte1.lower()
    message = ""
    for i in texte : 
        if i == " ":
            message += " "
        
        else : 
            if i == "w" :
                i = "v"
            

            result = np.where(carree == i)[0][0]
            message+=str(result)
            result = np.where(carree == i)[1][0]
            message+=str(result)

    print("text : ",texte1)
    print("message : ",message)

#if __name__ == '__main__':
crypte_polybe()