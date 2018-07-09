
def comparacion(D):
#lista1, lista2=[11,10,3,4],[1,3,4,6]
#print(lista1==lista2)

#print(lista1.sort(),lista1)
    print(D)
#    import string
#    dir(string)


def elimina_vocales(s):
    vocales = "aeiouAEIOU"
    s_sin_vocales = ""
    for letra in s:
        if letra not in vocales:
            s_sin_vocales += letra
    print(s_sin_vocales)
    return s_sin_vocales

def elimina_numeros(s):
    numeros="1234567890"
    s_sin_numeros=""
    for letra in s:
        if letra not in numeros:
            s_sin_numeros+= letra
#    print(s_sin_numeros)
 #   print(len(s_sin_numeros))
    return (s_sin_numeros)



def arreglo_disparos(Y):
    elimina_numeros(Y)
    Z = Y.replace(" ", "")#elimina espacios
    filas=len(Y)
    posicion_disparos=[]
#    for letra in Y:
 #       if letra
  #  for i range (filas):
   #     posicion_disparos.insert()

def area_barco(X):
    Letras=elimina_numeros(X)#trae la primer letra encontrada
    if Letras[0]!=Letras[1]:
        #print("son diferentes",Letras)
        indice1=X.index(elimina_numeros(X)[0])#trae el indice de la primera letra en la cadena X
        indice2 = X.index(elimina_numeros(X)[1])  # trae el indice de la segunda letra en la cadena X
    else:
#        print("son iguales",Letras)
        indice1 = X.index(elimina_numeros(X)[0])  # trae el indice de la primera letra en la cadena X
        indice2 =indice1+1+X[indice1+1:].index(elimina_numeros(X)[1])  # trae el indice de la segunda letra en la cadena X
    #print("indice2", indice2)

    #puntos de esquina 1
    Esq1_puntoY=X[:indice1]
    Esq1_puntoX=X[indice1]
    #puntos de esquina 2
    Esq2_puntoY = X[indice1+1:indice2]
    Esq2_puntoX = X[indice2]

    #print("EsqX",Esq2_puntoY,indice1,indice2)
    #print("punto",Esq1_puntoX, Esq1_puntoY, Esq2_puntoX, Esq2_puntoY)

    filas=int(Esq2_puntoY)-int(Esq1_puntoY)+1
    ABC="ABCDEFGHIJKLMNOPQRSTUVWXYZ" #declaración de vector de columnas para la posición de las letras
    columnas=ABC.index(Esq2_puntoX)-ABC.index(Esq1_puntoX)+1
    print(filas,columnas,filas*columnas)
    area_total=int(filas*columnas)
    pos_area=[]
    i=0
    ind=0
    for i in range(columnas):
        for j in range(filas):
            pos_area.insert(ind,str(int(Esq1_puntoY)+j)+ABC[ABC.index(Esq1_puntoX)+i])
            ind=ind+1

#    print("area",area_total,pos_area)
    return (pos_area)



N=4
B="1B 12C, 12D 22D,6G 17R "
D="2B 2D 3D 4A"
#comparacion(A)

#elimina_vocales(A)

Z=D.replace(" ","")#remplaza el caracter 1 por el 2 de la función replace
print(Z)

elimina_numeros(Z)

U=D.split(' ')#separa por arreglos por caracter en este caso espacio
print(U)

numero_barcos=B.count(",")+1 #saca el numero de barcos
print("#barcos",numero_barcos)
B=B.replace(" ","")#quitamos espacios en cadena
print(B)
esquinas=B.split(',')#arreglo esquinas de barcos
print("esquinas",esquinas)

barcos=[]
i=0
for i in range(numero_barcos):
   barcos.insert(i,area_barco(esquinas[i]))
   i+1
#    print(barcos[i])

#barcos.insert(0,area_barco(esquinas[0]))
#print(area_barco(esquinas[1]))
#print("Una Esquina:",area_barco(esquinas[1]))
#print(area_barco(esquinas[0]))
print("yyyy",barcos)

