num = int(input("Insira o numero: "))
fact = 1

if (num == 0):
    
    fact = 1

elif (num < 0):

    print("Nao sao permitidos valores negativos")

else:

    for i in range(num, 1, -1):
            
        fact *= i
    
    print(fact)
