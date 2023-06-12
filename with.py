nombre=input("Ingrese un nombre ")
edad=int(input("Ingrse su edad "))

textoEsc = nombre + " "+ str(edad)+  "\n"

with open("Usuarios.txt", "a") as a:
    a.write(textoEsc)
    # bla bla
    # bla

print("chau")