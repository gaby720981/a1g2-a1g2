def p1_resta (a, b, c):
    r = ((a-b)*c)
    return r

a = int(input("Ingrese un valor para A: "))
b = int(input("Ingrese un valor para B: "))
c = int(input("Ingrese un valor para C: "))
r = p1_resta (a, b, c)
print ("La resta entre A y B por C es igual a: ", r)