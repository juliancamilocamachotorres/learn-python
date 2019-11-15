#funcion que recibe la lista y el multiplicador
def multiplicador(lista,mult):
    for x in range (len(lista)):
        print(lista[x]*mult)

#
def creador():
    lista=[]
    for x in range (5):
        valor=int(input("ingrese el valor : "))
        lista.append(valor)
    multi=int(input("ingrese el multiplicador : "))
    multiplicador(lista,multi)

creador()