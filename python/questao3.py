#!/usr/bin/env python3
"""Sistema de cobrança de banho para um petshop

O petshop opera da seguinte maneira:

1. Para cães com peso menor que 3 kg o valor base é de 40 reais;
2. Para cães com peso igual ou maior que 3 kg e menor que 10 kg o valor base é de 50 reais;
3. Para cães com peso igual ou maior que 10 kg e menor que 30kg o valor base é de 60 reais;  
4. Para cães com peso igual ou maior que 30 kg e menor que 50kg o valor base é de 70 reais; 

5. Para cães com pelo curto (c) o multiplicador é 1;
6. Para cães com pelo médio (m) o multiplicador é 1.5;
7. Para cães com pelo longo (l) o multiplicador é 2;

8. Para o adicional de cortar unhas (1) do cachorro é cobrado um valor extra de 10 reais;
9. Para o adicional de escovar os dentes (2) do cachorro é cobrado um valor extra de 12 reais;
10. Para o adicional de limpar as orelhas (3) do cachorro é cobrado um valor extra de 15 reais;
11. Para o adicional de não querer mais nada (0) é cobrado um valor extra de 0 reais;

O valor final da conta é calculado da seguinte maneira: total = base * multiplicador + extra

Elabore um programa em Python que: 
 
1.	Realizar o print uma mensagem de boas-vindas que apareça o seu nome;
2.	Deve-se criar uma função chamada cachorro_peso() em que:
    a.	Pergunta o peso do cachorro;
    b.	Retorna o valor base com base no peso;
    c.	Repete a pergunta do item B.a se peso for igual ou acima 50kg;
    d.	Repete a pergunta do item B.a se digitar um valor não numérico;
3.	Deve-se criar uma função chamada cachorro_pelo() em que:
    a.	Pergunta o pelo do cachorro;
    b.	Retorna o multiplicador com base nos itens descritos no enunciado;
    c.	Repete a pergunta do item C.a se digitar uma opção diferente de: c/m/l;
4.	Deve-se criar uma função chamada cachorro_extra() em que:
    a.	Pergunta pelo serviço adicional;
    b.	Acumular o valor extra de cada adicional;
    c.	Repetir a pergunta item D.a enquanto não se digitar opção de: "não querer mais nada (0)";
    d.	Quando digitar o adicional não querer mais nada (0) retornar o valor extra;
5.	Deve-se calcular o total a pagar na parte do main conforme descrito no enunciado 
6.	Deve-se utilizar try/except
7.	Deve-se fazer comentários no código

1.	Deve-se colocar na apresentação de saída de console um pedido no qual o usuário digitou um valor não numérico para o peso
2.	Deve-se colocar na apresentação de console um pedido no qual o usuário digitou um valor acima 50 para o peso
3.	Deve-se colocar na apresentação de console um pedido no qual o peso e o tipo de pelo sejam válidos e com mais 2 extras
"""
__version__ = "0.1.0"
__author__ = "Giovanni Padilha"
__license__ = "Unlicensed"

# Começo - Função cachorro_peso()
# Retorna o valor da base com base no peso do cachorro
def cachorro_peso():
    base = None
    while True:
        
        # Validar se o valor não é numérico
        try:
            peso = float(input("Entre com o peso do cachorro: "))
            print()
        except ValueError as e:
            print("Você digitou um valor não numérico.")
            print("Por favor entre com o peso do cachorro novamente. \n")
            continue
        
        # Validar se o peso for maior que 50kg ou menor e igual a 0.
        if (peso >= 50):
            print("Não aceitamos cachorros tão grandes.")
            print("Por favor entre com o peso do cachorro novamente. \n")
            continue
        else:
            if peso < 3:
                base = 40
            elif peso >= 3 and peso < 10:
                base = 50
            elif peso >= 10 and peso < 30:
                base = 60
            else:
                base = 70
            break

    # Retornando o valor base e o peso do cachorro
    return base
# Fim - Função cachorro_peso()
 
# Começo - Função cachorro_pelo()       
# Retorna o multiplicador do preço com base no pelo do cachorro    
def cachorro_pelo():
    multiplicador = None
    while True:
        print("Entre com o pelo do cachorro: ")
        print("c - Pelo curto")
        print("m - Pelo médio")
        print("l - Pelo longo")
        pelo = input(">> ")
        print()
        
        # Validar se as opções do pelo inserido é válida
        if pelo == "c":
            multiplicador = 1.0
            break
        elif pelo == "m":
            multiplicador = 1.5
            break
        elif pelo == "l":
            multiplicador = 2.0
            break
        else:
            print("Você digitou um tipo de pelo não aceito.")
            print("Por favor entre com o pelo do cachorro novamente. \n")
            continue
    return multiplicador    
# Fim - Função cachorro_pelo()

# Começo - Função cachorro_extra()        
# Pergunta se o cliente quer serviços adicionais e retorna o valor total dos serviços
def cachorro_extra():
    extra = 0
    while True:
        print("Deseja adicionar mais algum serviço?")
        print("1 - Corte de Unhas - R$ 10,00")
        print("2 - Escovar Dentes - R$ 12,00")
        print("3 - Limpeza de Orelhas - R$ 15,00")
        print("0 - Não desejo mais nada")
        # Validar se o valor não é numérico
        try:
            adicional = int(input(">> "))
            print()
        except ValueError as e:
            print("Você digitou um valor não numérico.")
            print("Por favor entre com o serviço novamente. \n")
            continue
        
        # Validar se o serviço inserido está dentro das opções válidas
        if adicional == 1:
            extra = extra + 10
        elif adicional == 2:
            extra = extra + 12
        elif adicional == 3:
            extra = extra + 15
        elif adicional == 0:
            break
        else:
            print("Você digitou uma opção inválida.")
            print("Por favor entre com o serviço novamente. \n")
            continue
    return extra
# Fim - Função cachorro_extra()

print("Bem vindo ao Petshop de Giovanni Padilha")

# Desempacotando o valor da base e o peso da função cachorro_peso() nas variáveis "base" e "peso"
base = cachorro_peso()
multiplicador = cachorro_pelo()
extra = cachorro_extra()

# Cálculo do valor total da conta
total = (base * multiplicador) + extra

print(f"Total a pagar(R$): {total} (peso: {base} * pelo: {multiplicador} + adicional(is): {extra})")