###### EJERCICIO 1 ####
print("Vamos a calcular el área de un círculo")

def area_circulo():
    import math
    r=int(input("Introduce un radio:"))
    pi= math.pi
    AREA=pi*(r^2)
    print("Siendo la fórmula: pi*(r^2), el resultado del área, con radio {} es {}".format(r, AREA))
area_circulo()


###### EJERCICIO 2 ######

print("\n\n\n")
 
numeros=[]
def lee_numero(numeros):
    for x in range (3):
        numeros.append(int(input("Escribe un número:")))
        print(numeros)
lee_numero(numeros)
print("\n")
def mayor():
    if numeros[0]==numeros[1] or numeros[0]==numeros[2] or numeros[2]==numeros[1] or numeros[2]==numeros[1]==numeros[0]:
            mayorrep=max(numeros)
            print("Se repite algún número, pero el que mayor valor tiene es", mayorrep)
    else:
        mayor= max(numeros)
        print("El número con mayor valor de los tres, ha sido el {}".format(mayor))
mayor()


#### EJERCICIO 3 ####

print("\n\n\n")

def imc():
    weight=int(input("Introduzca su peso en kilogramos(Kg):"))
    height=round(float(input("Introduzca su altura en metros(m):")),  2)
    IMC= weight / (height**2)
    return IMC


def clasificacion(IMC):
    if IMC<18.5:
        print("Su IMC es {}, lo que implica que es menor de 18.5, siendo la clasificación de su IMC de 'Bajo Peso'".format(IMC))
    elif 18.5<=IMC<25.00:
        print("Su IMC es {}, lo que implica que está entre 18.5 y 25, siendo la clasificación de su IMC de 'Normal'".format(IMC))
    elif 25.00<=IMC<30.00:
        print("Su IMC es {}, lo que implica que está entre 25 y 30, siendo la clasificación de su IMC de 'Sobrepeso'".format(IMC))
    else:
        print("Su IMC es {}, lo que implica que es mayor que 30, siendo la clasificación de su IMC de 'Obesidad'".format(IMC))
clasificacion(imc())