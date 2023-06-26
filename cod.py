#ventas totales, venta total por año, venta promedio por año.
lista = []
venta_totales=0     
ventas_por_año={}
datos=open('datos.csv','r')
_ =datos.readline()

for linea in datos.readlines():
    datos_separados = linea.split(";")
    año=int(datos_separados[0])
    ventas_trismestrales =[int(valor) for valor in datos_separados [1:]]
    
    venta=sum(ventas_trismestrales)
    venta_totales += venta
    lista.append(datos_separados)

    if año in ventas_por_año:
        ventas_por_año[año]+= venta
    else:
        ventas_por_año[año]=venta
promedio=venta_totales//4

datos.close()
print("----------------------------------------")
print("La venta total es: ",venta_totales)
print("-----------------------------------------")
print("La venta promedio por año es: ",promedio )
print("-----------------------------------------")
print("Ventas por año: ")
for año, venta in ventas_por_año.items(): 
        print("Año", año, "-Ventas: ",venta)