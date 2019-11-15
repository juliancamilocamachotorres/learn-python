#program with for
n=int(input("cuantos triangulos : "))
a=0
for x in range(n):
    y=int(input("la base es : "))
    z=int(input("la altura es : "))
    print("base : ")
    print(y)
    print("altura : ")
    print(z)
    print("superficie : ")
    print((y*z)/2)
    if ((y*z)/2)>12 :
        a=a+1
print("la cantidad de superficies es mayor a 12 es : ")
print(a)
