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
