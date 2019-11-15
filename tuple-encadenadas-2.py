#cargar datos
def carga():
    lista=[]
    for x in range (3):
        nombre=input("nombre del candidato : ")
        cant=int(input("cantidad de provincias : "))
        provincias=[]
        for k in range(cant):
            numpro=input("nombre de la provincia : ")
            votos=int(input("cantidad de votos sacados en esta provincia : "))
            provincias.append((numpro,votos))
        lista.append((nombre,provincias))
    return lista

def imprimir(lista):
    for x in range(len(lista)):
        sumav=0
        for k in range (len(lista[x][1])):
            sumav=sumav+lista[x][1][k][1]
        print(lista[x][0],"tubo",sumav,"votos")

lista=carga()
imprimir(lista)