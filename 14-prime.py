def prime(num):

    if (num == 2):

        return print("É primo")

    elif (num % 2 != 0):

        return print("É primo")

    else:

        return print("Não é primo")

value = int(input("Insira o numero a ser consultado: "))

print(prime(value))
