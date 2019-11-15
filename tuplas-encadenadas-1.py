"""
Almacenar en una lista de 5 elementos los nombres de empleados de una empresa junto a sus últimos tres sueldos (estos tres valores en una tupla)
El programa debe tener las siguientes funciones:
1)Carga de los nombres de empleados y sus últimos tres sueldos.
2)Imprimir el monto total cobrado por cada empleado.
3)Imprimir los nombres de empleados que tuvieron un ingreso trimestral mayor a 10000 en los últimos tres meses.
"""
def carga():
    lista=[]
    for x in range(5):
        nombre=input("su nombre : ")
        sueldo1=int(input("su primer sueldo : "))
        sueldo2=int(input("su segundo sueldo : "))
        sueldo3=int(input("su tercer sueldo : "))
        print("----------------------------------")
        sueldos=(sueldo1,sueldo2,sueldo3)
        lista.append([nombre,sueldos])
    return lista
def monto(lista):

    for x in range(5):
        sum=0
        for y in range (3):
            sum=sum+lista[x][1][y]
        print(lista[x][0],"recibio en total",sum)

def mayores(lista):
    for x in range(5):
        sum=0
        for y in range (3):
            sum=sum+lista[x][1][y]
        if sum>10000:
            print(lista[x][0],"recibio en total",sum)
        

lista=carga()
print("----------------------------------")
monto(lista)
print("----------------------------------")
mayores(lista)