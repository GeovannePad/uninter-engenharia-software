#!/usr/bin/env python3
"""Loja

Se quantidade for menor que 200 o desconto será de 0%;
Se quantidade for igual ou maior que 200 e menor que 1000 o desconto será de 5%;
Se quantidade for igual ou maior que 1000 e menor que 2000 o desconto será de 10%;
Se quantidade for igual ou maior que 2000 o desconto será de 15%;

Realizar o print de uma mensagem de boas-vindas que apareça o seu nome
1 - Deve-se entrar com o valor unitário e quantidade do produto
2 - Deve-se retornar o valor total sem desconto e o valor total com desconto
3 - Deve-se utilizar as estruturas if, elif, else (todas elas)
4 - Deve-se fazer comentários no código

Deve-se colocar na apresentação de saíde de console um pedido de mais de 10 unidades.
"""
__version__ = '0.1.0'
__author__ = 'Giovanni Padilha'
__license__ = 'Unlicensed'

# Print da mensagem de Boas-vindas
print('Bem-vindo a Loja do Giovanni Padilha')

# Entrada do valor e a quantidade de produtos
produto_valor = float(input('Entre com o valor do produto: '))
produto_qtd = int(input('Entre com a quantidade do produto: '))

# Cálculo do valor total da compra
valor_total = produto_valor * produto_qtd
desconto = None

print(f'O valor SEM desconto: R$ {valor_total:.2f}')

# Cálculo e exibição do desconto

if produto_qtd < 200:
    print(f'O valor COM desconto: R$ {valor_total:.2f}')
# Desconto de 5%
elif produto_qtd >= 200 and produto_qtd < 1000:
    desconto = valor_total * 5/100
    print(f'O valor COM desconto: R$ {valor_total - desconto:.2f}')
# Desconto de 10%
elif produto_qtd >= 1000 and produto_qtd < 2000:
    desconto = valor_total * 10/100
    print(f'O valor COM desconto: R$ {valor_total - desconto:.2f}')
# Desconto de 15%
else:
    desconto = valor_total * 15/100
    print(f'O valor COM desconto: R$ {valor_total - desconto:.2f}')
