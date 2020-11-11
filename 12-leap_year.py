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
