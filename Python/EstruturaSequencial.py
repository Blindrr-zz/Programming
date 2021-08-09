import math

def Hello():

    return print("Alo mundo")

def Numero():

    numero = int(input("Insira um numero: "))

    return print("O numero inserido foi: ", numero)

def Media():

    nota  = list()
    nota.append(float(input("Insira sua nota: ")))
    nota.append(float(input("Insira sua nota: ")))
    nota.append(float(input("Insira sua nota: ")))
    nota.append(float(input("Insira sua nota: ")))

    media = sum(nota) / len(nota)

    return print("A sua media e: ", media)

def metroCentimetro():

    metro = float(input("Insira o valor em metros desejado: "))
    centimetro = metro * 100

    return print(centimetro)

def areaCirculo():

    raio = float(input("Insira o raio do circulo: "))
    area = math.pi * (raio * raio)
    
    return print(area)

def areaQuadrado2():

    lado = float(input("Insira o tamanho do lado: "))
    area = 2 * (lado * lado)

    return print(area)

def salario():

    hora = float(input("Quanto você ganha por hora? "))
    mes = float(input("Quantas horas voce trabalha por mes? "))
    salario = hora * mes

    return print(salario)

def fahrenheit():

    
    C = 5 * ((F-32) / 9)
