# Gabriel Correa dos Santos Barbosa

## Imprimir elementos da sequência de Fibonacci

# Definição: A sequência de Fibonacci (s[n]) é uma sequência de números inteiros positivos definida da seguinte forma:

# s[0] = 0; s[1] = 1; … ; s[n] = s[n-1] + s[n-2], n >= 2.

# Os 7 primeiros termos da sequência de Fibonacci são 0, 1, 1, 2, 3, 5 e 8.

# Desafio: Escreva um programa que receba como entrada um número inteiro n e imprima em uma linha os n primeiros termos da sequência de Fibonacci, separados por “; ”.

# - Exemplo: Para n = 5, a saída esperada é: "0; 1; 1; 2; 3"

dic_cache = {}

def fibonacci(n):
    if type(n) != int:
        raise TypeError("n must be an integer")
    if n < 1:
        raise ValueError("n must be an integer")
        
    if n in dic_cache:
        return dic_cache[n]

    if n == 1 or n == 2:
        value = 1
    elif n > 2:
        value = fibonacci(n-1) + fibonacci(n-2)

    dic_cache[n] = value
    return value


# Teste sequência até 1000

for n in range(1, 1001):
    print(f'ratio: {fibonacci(n+1) / fibonacci(n)}')
    print(f'{n} : {fibonacci(n)}')
