#funcion que recibe la lista y el multiplicador
def mostracaracteres(lista):
    mas=lista[0]
    for x in range (1,len(lista)):
        
        if len(mas)<len(lista[x]):
            mas=lista[x]
    print("el que tiene mas caracteres es : ")
    print(mas)

#crear la lista y el multiplicador y utilizarlo
def creador():
    lista=[]
    for x in range (6):
        valor=input("ingrese la palabra : ")
        lista.append(valor)
    mostracaracteres(lista)
    

creador()