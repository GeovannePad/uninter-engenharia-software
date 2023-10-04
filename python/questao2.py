#!/usr/bin/env python3
"""Sorveteria

A Sorveteria possui a seguite relação:

1. Bola de sorvete no sabor tradicional (tr) custa 6 reais, no sabor premium (pr) 7 reais e no especial (es) 8 reais;
2. Bolas de sorvete no sabor tradicional (tr) custam 11 reais, no sabor premium (pr) 13 reais e no especial (es) 15 reais;
3. Bolas de sorvete no sabor tradicional (tr) custam 15 reais, no sabor premium (pr) 18 reais e no especial (es) 21 reais;

Elabore um programa em Python que: 
 
1. Realizar o print uma mensagem de boas-vindas que apareça o seu nome;  
2. Deve-se entrar com o sabor (tr/pr/es) e o número de bolas de sorvete desejado (1/2/3)
3. Deve-se printar a mensagem de “Quantidade de Bolas de Sorvete Inválida". Se o usuário entrar com a quantidade de bolas de sorvete diferente de 1,2 e 3 repetir a partir do item A
4. Deve-se printar a mensagem de “Sabor de Sorvete Inválido" se o usuário entrar com um sabor diferente de tr (tradicional), pr (premium) e es (especial). Printar: e repetir a partir do item A
5. Deve-se perguntar se o cliente quer pedir mais alguma coisa. Se sim repetir a partir do item A, senão encerrar o programa printando o valor total
6. Deve-se utilizar as estruturas de while, break, continue (todas elas)
7. Deve-se fazer comentários no código

1. Deve-se colocar na apresentação de saída de console um pedido no qual o usuário errou ao digitar o sabor do sorvete
2. Deve-se colocar na apresentação de saída de console um pedido no qual o usuário errou ao digitar o número de bolas de sorvete
3. Deve-se colocar na apresentação de saída de console um pedido com duas opções sabores diferentes com quantidade de bolas diferentes 
"""
__version__ = "0.1.0"
__author__ = "Giovanni Padilha"
__license__ = "Unlicensed"

fechar_ordem = "s"
valor_total = 0

# Print da mensagens de Boas-vindas
print("Bem-vindo a Sorveteria do Giovanni Padilha")

# Início - Imprimindo a tabela com os valores dos sorvetes
print("{:-^91}".format("Cardápio"))
print("| {:^13} | {:^24} | {:^20} | {:^21} |".format("Nº DE BOLAS", "Sabor Tradicional (tr)", "Sabor Premium (pr)", "Sabor Especial (es)"))
print("| {:^13} | {:^24} | {:^20} | {:^21} |".format("1", "R$ 6,00", "R$ 7,00", "R$ 8,00"))
print("| {:^13} | {:^24} | {:^20} | {:^21} |".format("2", "R$ 11,00", "R$ 13,00", "R$ 15,00"))
print("| {:^13} | {:^24} | {:^20} | {:^21} |".format("3", "R$ 15,00", "R$ 18,00", "R$ 21,00"))
print("-" * 91)
# Fim - Imprimindo a tabela com os valores dos sorvetes

while fechar_ordem == "s":

    # Entrada do sabor do sorvete
    sabor = input("Entre com o sabor desejado (tr/pr/es): ")
    
    # Validação do sabor do sorvete
    if sabor == "tr" or sabor == "pr" or sabor == "es":
        
        # Entrada do número de bolas de sorvete
        numero_bolas = input("Entre com o número de bolas de sorvete desejado (1/2/3): ")
        
        # Validação do número de bolas de sorvete
        if numero_bolas == "1" or numero_bolas == "2" or numero_bolas == "3":
            
            # Início - Cálculo do valor do pedido
            numero_bolas = int(numero_bolas)
            valor_pedido = 0
            if sabor == "tr":
                sabor = "Tradicional"
                if numero_bolas == 1:
                    valor_pedido += 6
                elif numero_bolas == 2:
                    valor_pedido += 11
                else:
                    valor_pedido += 15
            elif sabor == "pr":
                sabor = "Premium"
                if numero_bolas == 1:
                    valor_pedido += 7
                elif numero_bolas == 2:
                    valor_pedido += 13
                else:
                    valor_pedido += 18
            else:
                sabor = "Especial"
                if numero_bolas == 1:
                    valor_pedido += 8
                elif numero_bolas == 2:
                    valor_pedido += 15
                else:
                    valor_pedido += 21     
            # Fim - Cálculo do valor do pedido 
        else:
            print("Quantidade de bolas de sorvete inválida. Tente novamente \n")
            continue
    else:
        print("Sabor de sorvete inválido. Tente novamente \n")
        continue
    
    print(f"Você pediu {numero_bolas} bolas de sorvete no sabor {sabor}: R$ {valor_pedido:.2f}")
    valor_total += valor_pedido
    fechar_ordem = input("Deseja pedir mais algum sorvete? (s/n): ")
    print()

print(f"O valor total a ser pago: R$ {valor_total:.2f}")