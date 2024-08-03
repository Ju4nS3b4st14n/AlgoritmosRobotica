# MENU ELECCION ROBOTS
print("ROBOTS")
print("1.ROBOT CILINDRICO\n2.ROBOT CARTESIANO\n3.ROBOT ESFERICO")

Eleccion = int(input("Digite el numero del robot del que quiere saber sus articulaciones: "))

if Eleccion == 1 :
        print("EL ROBOT CILINDRICO TIENE 1 ARTICULACION ROTACIONAL Y 2 ARTICULACIONES PRISMATICAS")
        
elif Eleccion == 2:
        print("EL ROBOT CARTESIANO TIENE 3 ARTICULACIONES PRISMATICAS")
        
elif Eleccion == 3:
        print("EL ROBOT ESFERICO TIENE 2 ARTICULACIONES ROTACIONALES Y 1 ARTICULACION PRISMATICA")