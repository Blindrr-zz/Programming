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

print(teste)