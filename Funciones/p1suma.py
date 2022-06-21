def p1_suma (a, b, c):
    s = ((a+b)*c)
    return s

a = int(input("Ingrese un valor para A: "))
b = int(input("Ingrese un valor para B: "))
c = int(input("Ingrese un valor para C: "))
s = p1_suma (a, b, c)
print ("La suma entre A y B por C es igual a: ", s)