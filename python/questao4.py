#!/usr/bin/env python3
"""Controle de Colaboradores

Este software deve ter o seguinte menu e opções:

1) Cadastrar Colaborador
2) Consultar Colaborador
    1. Consultar Todos 
    2. Consultar por Id;
    3. Consultar por Setor;
    4. Retornar ao menu;
3) Remover Colaborador
4) Encerrar Programa

Elabore um programa em Python que:

1. Realizar o print uma mensagem de boas-vindas que apareça o seu nome;
2. Deve-se criar uma lista vazia com o nome de lista_colaboradores e a variável id_global com valor inicial igual a 0
3. Deve-se criar uma função chamada cadastrar_colaborador(id) em que:
    a. Pergunta nome, setor, pagamento do colaborador;
    b. Armazena o id (este é fornecido via parâmetro da função), nome, setor, salário dentro de um dicionário;
    c. Copiar o dicionário dentro para dentro da lista_colaboradores;
4. Deve-se criar uma função chamada consultar_colaborador() em que:
    a. Deve-se pergunta qual opção deseja (1. Consultar Todos / 2. Consultar por Id / 3. Consultar por Setor / 4. Retornar ao menu) e   realizar o print “Opção inválida" se entrar com valor diferente de 1, 2, 3 ou 4:
        i. Se Consultar Todos, apresentar todos os colaboradores com todos os seus dados cadastrados;
        ii. Se Consultar por Id, apresentar o colaborador específico com todos os seus dados cadastrados;
        iii. Se Consultar por Setor, apresentar todos os colaboradores do setor específico com todos os seus dados cadastrados;
        iv. Se Retornar ao menu, deve-se retornar ao menu principal
5. Deve-se criar uma função chamada remover_colaborador() em que:
    a. Deve-se pergunta pelo id do colaborador a ser removido;
    b. Remover o colaborador da lista_colaboradores;
6. Deve-se criar uma estrutura de menu no main em que:
    a. Deve-se pergunta qual opção deseja (1. Cadastrar Colaborador / 2. Consultar Colaborador / 3. Remover Colaborador / 4. Encerrar Programa) e realizar o print “Opção inválida" se entrar com valor diferente de 1, 2, 3 ou 4:
        i. Se Cadastrar Colaborador, acrescentar em um a variavel id_ global e chamar a função cadastrar_colaborador(id_ global);
        ii. Se Consultar Colaborador, chamar função consultar_colaborador();
        iii. Se Remover Colaborador, chamar função remover_colaborador();
        iv. Se Encerrar Programa, sair do menu (e com isso acabar a execução do código);
7. Deve-se utilizar lista de dicionários (uma lista contento dicionários dentro)
8. Deve-se fazer comentários no código

1. Deve-se colocar na apresentação de saída de console o cadastro de 3 colaboradores (sendo 2 deles no mesmo setor)
2. Deve-se colocar na apresentação de saída de console a consulta de todos os colaboradores
3. Deve-se colocar na apresentação de saída de console a consulta por código de um dos colaboradores
4. Deve-se colocar na apresentação de saída de console a consulta por setor em que 2 colaboradores façam parte
5. Deve-se colocar na apresentação de saída de console a remoção de um dos colaboradores e na sequência a consulta de todos os colaboradores
"""
__version__ = "0.1.0"
__author__ = "Giovanni Padilha"
__license__ = "Unlicensed"

# Começo - Função exibir_colaborador()
# Função que exibe os dados formatados de um colaborador
def exibir_colaborador(colaborador):
    print(f"ID: {colaborador['id']}")
    print(f"Nome: {colaborador['nome']}")
    print(f"Setor: {colaborador['setor']}")
    print(f"Pagamento: R$ {colaborador['pagamento']:.2f}")
    print("-" * 40)
# Fim - Função exibir_colaborador()

# Começo - Função cadastrar_colaborador()
# Função para cadastrar um colaborador
def cadastrar_colaborador(id):
    colaborador = {
        "id": None,
        "nome": None,
        "setor": None,
        "pagamento": None,
    }
    
    print("*" * 80)
    print("{:-^80}".format("MENU CADASTRAR COLABORADOR"))
    print(f"ID do colaborador {id}")

    # Entrada de dados - nome, setor e pagamento do colaborador
    nome = input("Por favor entre com o nome: ")
    setor = input("Por favor entre com o setor: ")
    pagamento = input("Por favor entre com o pagamento (R$): ")
    
    # Atribuindo as variáveis com os dados inseridos pelo usuário no dicionário colaborador[]
    colaborador["id"] = id
    colaborador["nome"] = nome
    colaborador["setor"] = setor
    colaborador["pagamento"] = float(pagamento)
    
    lista_colaboradores.append(colaborador) # Armazenando o id, nome, setor e salário do colaborador dentro de um dicionário
# Fim - Função cadastrar_colaborador()

# Começo - Função consultar_colaborador()
# Função para consultar colaboradores de diferentes formas
def consultar_colaborador():
    while True:
        
        # Opções para pesquisar colaboradores
        print("*" * 80)
        print("{:-^80}".format("MENU CONSULTAR COLABORADOR"))
        print("Escolha a opção desejada:")
        print("1-Consultar Todos os Colaborador")
        print("2-Consultar Colaborador por ID")
        print("3-Consultar Colaborador(es) por setor")
        print("4-Retornar")
        
        # Verificação se a opção é numérica
        try:
            opcao_consulta = int(input(">> "))
        except ValueError as e:
            print("Você digitou um valor não numérico.")
            print("Digite outra opção")
            continue
        
        # Consultar todos os colaboradores
        if opcao_consulta == 1:
            print("-" * 40)
            for colaborador in lista_colaboradores:
                exibir_colaborador(colaborador)
        # Consultar colaborador por id
        elif opcao_consulta == 2:
            id_colaborador = int(input("Entre com o ID do colaborador a ser pesquisado: "))
            print("-" * 40)
            for colaborador in lista_colaboradores:
                if colaborador.get("id") == id_colaborador:
                    exibir_colaborador(colaborador)
                    break
        # Consultar colaborador(es) por setor
        elif opcao_consulta == 3:
            setor_colaborador = input("Entre com o Setor que desejado ser pesquisado: ")
            print("-" * 40)
            for colaborador in lista_colaboradores:
                if colaborador.get("setor") == setor_colaborador:
                    exibir_colaborador(colaborador)
        # Retornar ao menu principal            
        elif opcao_consulta == 4:
            break    
        else:
            # Opção inválida
            print("Você digitou uma opção inválida")
            print("Digite outra opção")
            continue
# Fim - Função consultar_colaborador()

# Começo - Função remover_colaborador()
# Função para remover um colaborador pelo id
def remover_colaborador():
    id_colaborador = int(input("Entre com o ID do colaborador a ser removido: "))
    for colaborador in lista_colaboradores.copy():
        if colaborador.get("id") == id_colaborador:
            lista_colaboradores.remove(colaborador) # Removendo o colaborador
            break
# Fim - Função remover_colaborador()

# Começo - Estrutura de menu
lista_colaboradores = [] # Lista vazio que vai armazenar os colaboradores
id_global = 0 # Variável id_global com o valor inicial igual a 0

print("Bem-vindo ao Controle de Colaboradores do Giovanni Padilha") # Print da mensagem de Boas-vindas contendo o meu nome

while True:
    print("*" * 80)
    print("{:-^80}".format("MENU PRINCIPAL"))
    print("Escolha a opção desejada:")
    print("1-Cadastrar Colaborador")
    print("2-Consultar Colaborador(es)")
    print("3-Remover Colaborador")
    print("4-Sair")

    # Validando se a opção inserida é numérica
    try:
        opcao = int(input(">> "))
    except ValueError as e:
        print("Você digitou um valor não numérico.")
        print("Digite outra opção")
        continue
    
    # Cadastrar colaborador
    if opcao == 1:
        id_global = id_global + 1
        cadastrar_colaborador(id_global)
    # Consultar colaborador
    elif opcao == 2:
        consultar_colaborador()
    # Remover colaborador
    elif opcao == 3:
        remover_colaborador()
    # Encerrar programa
    elif opcao == 4:
        break
    else:
        # Opção inválida
        print("Você digitou uma opção inválida")
        print("Digite outra opção")
# Fim - Estrutura de menu