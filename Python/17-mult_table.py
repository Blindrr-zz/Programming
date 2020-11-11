def multi_Table(num):

    multi_Table = list()
    for i in range(0, 11):

        res = i*num
        multi_Table.append(res)
    
    return multi_Table

value = int(input("Insira o numero da tabuada desejada: "))

print(multi_Table(value))