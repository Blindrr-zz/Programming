def check(num):

    if (num > 0):

        return print("É positivo")

    elif (num == 0):

        return print("É zero")

    else:

        return print("É negativo")

val = int(input("Insira o número a ser consultado: "))

print(check(val))
def isEven(num):

    if (num % 2 == 0):

        return print("É par")

    else:

        return print("É impar")

value = float(input("Insira o valor a ser consultado: "))

print(isEven(value))
def leap(year):

    if (year > 2020):

        if ((year - 2020) % 4 == 0):

            return print("É bissexto")

        else:

            return print("Não é bissexto")

    else:

        if ((2020 - year) % 4 == 0):

            return print("É bissexto")

        else:

            return print("Não é bissexto")

value = int(input("Insira o ano a ser consultado: "))

print(leap(value))
lista = list()

for i in range(0, 3):

    valor = int(input("Insira o numero na lista: "))
    lista.append(valor)

print(max(lista))
def prime(num):

    if (num == 0 | num == 1):

        return print("Não é primo")

    elif ((num == 2) | (num == 3) | (num == 5) | (num == 7)):

        return print("É primo")

    elif ((num % 2 != 0) & (num % 3 !=0) & (num % 5 !=0) & (num % 7 !=0)):

        return print("É primo")

    else:

        return print("Não é primo")

value = int(input("Insira o numero a ser consultado: "))

prime(value)
def prime(num):

    if (num == 0 | num == 1):

        return False

    elif ((num == 2) | (num == 3) | (num == 5) | (num == 7)):

        return True

    elif ((num % 2 != 0) & (num % 3 !=0) & (num % 5 !=0) & (num % 7 !=0)):

        return True

    else:

        return False

def check(lista):

    primes = list()
    for i in lista:

        if (prime(i)):

            primes.append(i)

    return primes

def fazLista(a, b):

    lista = list()
    for i in range(a, b):

        lista.append(i)

    return lista

intervalo1 = int(input("Insira o primeiro intervalo: "))
intervalo2 = int(input("Insira o segundo intervalo: "))
teste = check(fazLista(intervalo1, intervalo2))

print(teste)num = int(input("Insira o numero: "))
fact = 1

if (num == 0):
    
    fact = 1

elif (num < 0):

    print("Nao sao permitidos valores negativos")

else:

    for i in range(num, 1, -1):
            
        fact *= i
    
    print(fact)
def multi_Table(num):

    multi_Table = list()
    for i in range(0, 11):

        res = i*num
        multi_Table.append(res)
    
    return multi_Table

value = int(input("Insira o numero da tabuada desejada: "))

print(multi_Table(value))def check(num):

    arms = str(num)

    dig1 = int(arms[0])
    dig2 = int(arms[1])
    dig3 = int(arms[2])

    chck = dig1 ** 3 + dig2 ** 3 + dig3 ** 3

    if (chck == num):

        return print("É armstrong")

    else:

        return print("Não é armstrong")

value = int(input("Insira o numero a ser consultado: "))

check(value)def check(num):

    arms = str(num)

    dig1 = int(arms[0])
    dig2 = int(arms[1])
    dig3 = int(arms[2])

    chck = dig1 ** 3 + dig2 ** 3 + dig3 ** 3

    if (chck == num):

        return print("É armstrong")

    else:

        return print("Não é armstrong")

value = int(input("Insira o numero a ser consultado: "))

check(value)print("Hello World")
val1 = int(input("Insira o primeiro numero: "))
val2 = int(input("Insira o segundo numero: "))

add = val1 + val2

print(add)
import math

num = int(input("Insira o numero a ser tirado a raiz: "))

print(math.sqrt(num))
base = int(input("Insira a base do triangulo: "))
height = int(input("Insira a altura do triangulo: "))

print((base*height)/2)
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
var1 = input("Insira a primeira variavel: ")
var2 = input("Insira a segunda variavel: ")

temp = var1
var1 = var2
var2 = temp

print("Variavel 1 = " + var1)
print("Variavel 2 = " + var2)
import random

print(random.randint(0, 10))
def convert(mi):

    return mi * 1.609

val = float(input("Insira a milhagem: "))

print("A quilometragem é aproximadamente: "+ str(convert(val)))
def convert(temp):

   return (temp * 9/5) + 32

val = float(input("Insira a temperatura em celsius: "))

print("A temperatura em Fahrenheit é: " + str(convert(val)) + " F°")
