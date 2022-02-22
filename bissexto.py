## Verificar se um ano é bissexto

# Definição: Chama-se ano bissexto o ano ao qual é acrescentado um dia extra, ficando com 366 dias, um dia a mais do que os anos normais de 365 dias, ocorrendo a cada quatro anos, exceto anos múltiplos de 100 que não são múltiplos de 400.

# Desafio: Escreva um programa que receba um número inteiro positivo representando um ano e determine se esse é um ano bissexto.

def ano(n):

    restrição = n % 4 == 0 and (n % 100 == 0 or n % 400 != 0)

    if restrição:
        return f"O ano {n} é bissexto"
    
    return f"O ano {n} não é bissexto"


# Testes

print(ano(1988)) # True
print(ano(2000)) # True
print(ano(1946)) # False
print(ano(1977)) # False