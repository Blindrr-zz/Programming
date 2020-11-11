def prime(num):

    if (num == 2):

        return True

    elif (num % 2 != 0):

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