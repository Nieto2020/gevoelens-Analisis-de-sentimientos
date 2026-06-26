#LISTAS
POSITIVE_LIST = ["good", "nice", "awesome", "genius", "fun", "amazing"]
NEGATIVE_LIST = ["bad", "horrible", "boring", "terrible", "awful", "shit"]



def analizar_sentimiento(comment):
    if len(comment) > 5 and len(comment) < 100:
        comment.lower()
        comment.replace(" ", "-")
    else:
        print("ERROR...Longitud no aceptada.")