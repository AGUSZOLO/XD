# Escribir un algoritmo que almacene en un archivo datos de alumnos
# de BDI. almacena : 1.nombre, apellido   2.DNI    3. nota de los 6 tp 5,9,10,2,3,4  
# 4 nota final de aprobacion/desaprobacion
#Menu permita ingresar(estudiante), nota de los practicos
#muestra estudiante aprobado/desaprobadoc
datos=open("datos","a")
notas= []
alumnos= []
aprobados=[]
desaprobados=[]
suma=0


while True:
    print("===================")
    print("Menu de opciones: ")
    print("1.Ingresar Alumnos")
    print("2.Ingresar Notas de los TP")
    print("3.Salir (al salir de podra ver el resultado de sus alumnos)")
    print("=====================")

    opcion=input("Selecione una opcion: ")

    if opcion == "1":
        cantidad=int(input("Ingrese la cantiadad de alumos que quiere registrar: "))

        for i in range (0,cantidad): 
            nom=input("Ingese su nombre: ")
            ape=input("Ingrese su apellido: ")
            dni=int(input("Ingrese su Dni: "))
            alumnos.append((nom, ape, dni))

        input("Alumnos ingresados. Presione enter para continuar...")
        continue

    elif opcion == "2":
        if not alumnos:
            print("No se han ingresado alumnos. Porfavor, ingresea alumnos primero")
            input("Presione Enter para continuar...")
            continue

        for i in range(len(alumnos)):
            alumno = alumnos[i]
            nom=alumno[0]
            ape=alumno[1]
            dni=alumno[2]
            print(f"Ingrese las notas de los Tp para el almuno {nom} {ape} : ")
            tp_notas=[]
            for j in range (6):
                nota= int(input(f"Nota del TP {j+1}: "))
                tp_notas.append(nota)
                suma+=nota
            notas.append(tp_notas)

        input("Notas Ingresadas. Presione Enter para continuar...")
        continue

    elif opcion == "3":
        print("Saliendo del programa...")
        break

    else:
        print("Opcion invalida.Porfavor seleccione una opcion valida")

print("=============================================")
print("Alumos aprobados: ")
for a in range (len(alumnos)):
    alumno=alumnos[a]
    nom=alumno[0]
    ape=alumno[1]
    dni=alumno[2]
    promedio= sum(notas[a]) / len(notas[a])
    if promedio >= 6:
        print(f"{nom} {ape} - Promedio : {promedio: .2f}")
print("=================================================")

print("Alumnos desaprobados: ")
for a in range(len(alumnos)):
    alumno=alumnos[a]
    nom=alumno[0]
    ape=alumno[1]
    dni=alumno[2]
    promedio= sum(notas[a]) / len(notas[a])
    if promedio < 6:
        print(f"{nom} {ape} - Promedio: {promedio: .2f}")
print("=====================================================")
datos.close()