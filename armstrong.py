# Gabriel Correa dos Santos Barbosa

## Verificar se um número é um número de Armstrong

# Definição: Um número inteiro positivo x de n algarismos é um número de Armstrong de ordem n se x é igual a soma das n-ésimas potências de seus algarismos.

# - Exemplo 1: x = 153; n = 3: x é um número de Armstrong de ordem 3, pois x = 1^3 + 5^3 + 3^3.
# - Exemplo 2: x = 13; n = 2: x não é um número de Armstrong de ordem 2, pois x != 1^2 + 3^2.

# Desafio: Escreva um programa que determine se um número é um número de Armstrong e determine sua ordem.


def checar_armstrong(x):
    str_x = str(x)
    map_x = map(int, str_x)
    list_x = list(map_x)
    n = len(list_x)

    value = 0
    for i in list_x:
        value += i**n

    if value == x:
        return f'O número {x} é de ordem {n}'
    else:
        return f'O número {x} não é de ordem {n}'

# Testes
print(checar_armstrong(0))
print(checar_armstrong(1))
print(checar_armstrong(2))
print(checar_armstrong(3))
print(checar_armstrong(4))
print(checar_armstrong(5))
print(checar_armstrong(6))
print(checar_armstrong(7))
print(checar_armstrong(8))
print(checar_armstrong(9))
print(checar_armstrong(153))
print(checar_armstrong(370))
print(checar_armstrong(371))
print(checar_armstrong(407))