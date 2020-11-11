def check(num):

    if (num > 0):

        return print("É positivo")

    elif (num == 0):

        return print("É zero")

    else:

        return print("É negativo")

val = int(input("Insira o número a ser consultado: "))

print(check(val))
