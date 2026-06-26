import re


def analizar_sentimiento(comment):
    if len(comment) > 5 and len(comment) <= 100:
        comment.lower()
        comment = re.sub(r"[-_?¿!¡,.#$%&/()']", " ", comment)
        fcom = comment.split()
        return fcom
    else:
        print("ERROR...Longitud no aceptada.")