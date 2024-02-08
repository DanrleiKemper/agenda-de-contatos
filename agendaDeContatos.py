#Variavel para armazenar os contatos / criação de uma lista
contatos = []

#Menu da Agenda
while True:
    print("Bem Vindo a Sua agenda de contatos\n")
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

    if escolha == "8":
        print("PROGRAMA FINALIZADO!")
        break

#print("PROGRAMA FINALIZADO!")