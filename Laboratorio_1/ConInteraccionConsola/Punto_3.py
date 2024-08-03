import math
pi = math.pi

print("1. Prisma\n2. Piramide\n3. Cono truncado\n4. Cilindro\n")

Eleccion = int(input("Ingrese el numero del solido: "))

if Eleccion==1:
    print("PRISMA\n")
    Base = float(input("Digite el valor del area de la base del prisma (m^2): "))
    Altura = float(input("Digite el valor de la altura del prisma (m): "))
    Vprisma = Base * Altura 
    print("\nEl volumen del prisma es: ", Vprisma)

elif Eleccion==2:
    print("PIRAMIDE\n")
    Base = float(input("Digite el valor del area de la base de la piramide (m^2): "))
    Altura = float(input("Digite la altura de la piramide (m): "))
    VPiramide = (Base * Altura)/3
    print("\nEl volumen de la piramide es: ", VPiramide) 

elif Eleccion==3:
    print("CONO TRUNCADO\n")
    Altura = float(input("Digite la altura del cono truncado (m): "))
    Radio1 = float(input("Digite el radio de la base del cono (m): "))
    Radio2 = float(input("Digite el radio de la punta del cono (m): "))
    Vcono = ((Altura*pi)/3)*((math.pow(Radio1,2))+(math.pow(Radio2,2))+(Radio1*Radio2))
    print("\nEl volumen del cono es: ", Vcono) 

elif Eleccion==4:
     print("CILINDRO\n")
     Altura = float(input("Digite la altura del cilindro (m): "))
     Radio1 = float(input("Digite el radio del cilindro (m): "))
     Vcilindro = (pi)*(math.pow(Radio1,2))*(Altura)
     print("\nEl volumen del cilindro es: ", Vcilindro) 