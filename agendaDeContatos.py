#Finção para adicionar os dados do contato
def adicionar_contato(contatos, nome_contato, telefone_contato, email_contato):
    novo_contato = {"Nome": nome_contato, "Telefone": telefone_contato, "E-mail": email_contato}
    contatos.append(novo_contato)
    #print(f"Contato: {nome_contato} {telefone_contato} {email_contato} foi adicionado com sucesso!")
    print("Contato foi adicionado com sucesso!")
    return

#função para visualizar contato adicionado
def visualizar_contato(contatos):
    print("\nLista de Contatos adicionados")

    # start=1 = usado para começão a exibir as tarefas no indice 1 e não zero
    for i, contato in enumerate(contatos, start=1):
        print(f"{i} - Nome: {contato['Nome']} | Telefone: {contato['Telefone']} | E-mail: {contato['E-mail']}")
    return

#função para atualizar um contato
def editar_contato(contatos, indice_contato, nome_contato, telefone_contato, email_contato):
    '''
        Condição para validar a alteração do contato. 
        Se o usuário informar o indice correto, programa faz a execução
        Caso contrário, programa para a execução (cai no else)
    '''
    if indice_contato >= 0 and indice_contato < len(contatos):
        contatos[indice_contato]["Nome"] = nome_contato
        contatos[indice_contato]["Telefone"] = telefone_contato
        contatos[indice_contato]["E-mail"] = email_contato
        print("Contato editado com sucesso!")
    else:
        print("Índice de contato inválido!")


#Variavel para armazenar os contatos / criação de uma lista
contatos = []

#Menu da Agenda
while True:
    print("\nBem Vindo a Sua agenda de contatos\n")
    print("##### MENU ####")

    print("1 - Adicionar um contato")
    print("2 - Visualizar sua lista de contatos")
    print("3 - Editar um contato")
    print("4 - Marcar um contato como favorito")
    print("5 - Desmarcar um contato como favoritado")
    print("6 - Visualizar a lista de contatos favoritados")
    print("7 - Deletar/excluir um contato")
    print("8 - Sair")

    escolha = input("Digite sua escolha: ")

    if escolha == "1":
        nome_contato = input("Nome: ")
        telefone_contato = input("Telefone: ")
        email_contato = input("E-mail: ")
        adicionar_contato(contatos, nome_contato, telefone_contato, email_contato)

    elif escolha == "2":
        vizualizar_contato(contatos)

    elif escolha == "3":
        vizualizar_contato(contatos)
        indice_contato = int(input("Informe o idice do contato que deseja editar: ")) -1
        nome_contato = input("Novo nome: ")
        telefone_contato  = input("Novo telefone: ")
        email_contato  = input("Novo e-mail: ")
        editar_contato(contatos, indice_contato, nome_contato, telefone_contato, email_contato)


    elif escolha == "8":
        print("PROGRAMA FINALIZADO!")
        break

#print("PROGRAMA FINALIZADO!")