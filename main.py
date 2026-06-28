import inicializar as pr

#comentario de prueba
comentario = "This game is amazing, cant believe it. Expecting a dlc"

list = pr.limpieza(comentario)
sentiment, score = pr.scoring(list)

pr.guardar_analisis(comentario, sentiment, score)
