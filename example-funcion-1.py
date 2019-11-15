#determinamos el menor valor
def insert():
    lista=[]
    for x in range (3):
        valor=int(input("ingrese el valor : "))
        lista.append(valor)
    determinar(lista)
     
def determinar(lista):
    
    #ingresa el valor
    menor=lista[0]
    for k in range (1,3):
        if menor>lista[k]:
            menor=lista[k]
    
    print("el menor es : ")
    print(menor)

insert()
insert()