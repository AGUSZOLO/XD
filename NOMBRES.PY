archivo=open("Guardado.txt", "a")
diccionario={}

for i in range (4):
    nom=input("Ingrese nombre: ")
    edad=int(input("Ingrese la Edad: "))
    diccionario[nom]=edad
archivo.write(f"nombre: {nom}, Edad:{edad}\n")
for nom, edad in diccionario.items():
    print(nom, edad)
    

selec=input("Seleccione el nombre: ")

while True: 
        print("Menu de movimientos: ")
        print("1.Despedir")
        print("2.Renovacion")
        print("3.Aumento")
        print("4.Asenso")
        print("5.Salir")
        break

opcion= input("Seleccione una: ")

if opcion == "1":
    print("Selecciono el 1, despidio a: ", selec)
elif opcion == "2":
    print("Selecciono la opcion 2, ¿de cuantos años quiere la renovacion? ")
    rev=int(input("Ingrese los años: "))  
    print("Se renovo el contracto a",rev, "años")
elif opcion == "3":
    print("Selecciono la opcion 3 ¿De cuanto es el aumento a",selec,"?")
    aum=int(input("Ingrese la cantidad a aumentar: "))
    print("Se aumento correctamente a un ",aum,"%")
elif opcion == "4":
    print("Selecciono la opcion 4 ¿A que rango quiere el Asenso")
    asen=input("Ingrese el rango: ")
    print("Se asendio correctamente a ",asen)
elif opcion == "5":
        print("Salio del programa")

else:
        print("Opcion incorrecta")    

archivo.close() 