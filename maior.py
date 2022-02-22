## Encontrar o maior número entre três números

# Desafio: Escreva um programa que receba três números e encontre o maior dentre eles, sem utilizar rotinas builtin (por exemplo, rotina max do Python).

def achar_maior(n_1, n_2, n_3):

    lista = [n_1, n_2, n_3]
    
    for i in range(len(lista)):
        for x in range(i+1, len(lista)):
            if lista[i] > lista[x]:
                highest_value = lista[i]
            else:
                highest_value = lista[x]

    return highest_value


# Testes

print(achar_maior(146,595,128))
print(achar_maior(65146,5541695,515128))
print(achar_maior(14632,59523,128654))
print(achar_maior(14643,59345,12854))
print(achar_maior(146556,59534,128646))
