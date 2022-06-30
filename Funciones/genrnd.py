# -*- coding: utf-8 -*-


#La función genrnd genera una lista de 50 números flotantes 
#entre los argumentos a (límite inferior) y b (límite superior). Dicha lista se
#llama num_rand


import random
num_rand = []

def genrnd(a, b):
    for i in range(50):
        num_rand.append(random.uniform(a,b))
        
        
genrnd(100, 200)
print(num_rand)