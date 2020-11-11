import math

def discriminante(a, b, c):
    
    return b*b - 4*a*c

def quadratica(a, b, c):

    bhsk1 = (b * -1) + math.sqrt(discriminante(a, b, c))
    raiz1 = bhsk1 / (2 * a)
    bhsk2 = (b * -1) - math.sqrt(discriminante(a, b, c))
    raiz2 = bhsk2 / (2 * a)

    return raiz1, raiz2

print(quadratica(2, 4, -6))
