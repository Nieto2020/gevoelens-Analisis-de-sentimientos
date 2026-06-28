import re

#Regresa un a lsta con palabras individuales

def limpieza(comment):
    if len(comment) > 5 and len(comment) <= 100:
        comment.lower()
        comment = re.sub(r"[-_?¿!¡,.#$%&/()']", " ", comment)
        lcom = comment.split()
        return lcom
    else:
        print("ERROR...Longitud no aceptada.")