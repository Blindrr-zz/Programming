def check(num):

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

check(value)