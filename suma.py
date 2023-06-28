
def suma (*args):
    s=0
    for arg in args:
        s += arg
    return s

resultado=suma(1,3,5,2,7,9,10,10)
print(resultado)