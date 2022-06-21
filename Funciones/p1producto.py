def p1_producto (a, b, c):
    p = (a*b+c)
    return p

a = int(input("Ingrese un valor para A: "))
b = int(input("Ingrese un valor para B: "))
c = int(input("Ingrese un valor para C: "))
p = p1_producto (a, b, c)
print ("El producto entre A y B más C es igual a: ", p)