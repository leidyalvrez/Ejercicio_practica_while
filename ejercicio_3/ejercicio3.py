import random

numero = random.randint(1,100)
intento = 0 

while intento!= numero:
    intento = int(input("Adivina el numero desde el 1 hasta el 100: "))

    if intento < numero:
        print("El numero es mas alto")
    elif intento > numero:
        print("El numero es mas bajo")

print("FELICIDADES HAS ADIVINADO EL NUMERO :")

