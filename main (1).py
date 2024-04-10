# Gestão de Negócios
# Exemplo de cadastro de cliente

def cadastro_cliente():
    nome = input("Nome: ")
    cpf = input("CPF: ")
    endereco = input("Endereço: ")
    email = input("E-mail: ")
    telefone = input("Telefone: ")

    # Aqui você pode armazenar esses dados em um arquivo, banco de dados, etc.

    print("Cliente cadastrado com sucesso!")


# Menu principal
def main_menu():
    print("Menu de Opções:")
    print("1 - Cadastrar Cliente")
    print("2 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == '1':
        cadastro_cliente()
    elif opcao == '2':
        print("Até logo!")
    else:
        print("Opção inválida!")


# Início do programa
main_menu()
