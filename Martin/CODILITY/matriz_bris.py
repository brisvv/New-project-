import math

def ejemplo():
    key = input('Key: ') #Pedimos la clave
    text = input('Text: ') #Pedimos una cadena de texto
    text_c = list(text)   #Pasamos la cadena a una lista de caracteres
    while ' ' in text_c:  #quitamos espacios
      text_c.remove(' ')
    while '12345'
    #caculo de las columnas y renglones
    columns = len(key)
    rows = int(math.ceil(float(len(text_c)) / float(len(key))) )
    print(rows)
    print(columns)
    #Definicion de una matriz
    matrix = []
    pos = 0

    #Agregar los caracteres
    for i in range(rows):
        matrix.append([])
        for j in range(columns):
            #Agregar en la fila i una nueva columna con el siguiente caracter
            #     o None si ya no quedan
            matrix[i].append(text_c[pos] if pos < len(text_c) else None)
            #Incrementar el contador de caracteres
            pos += 1

    print (matrix)

ejemplo()

