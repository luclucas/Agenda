from prettytable import PrettyTable
from csv import DictReader


class Contato:
    def __init__(self, nome, telefone, email, twitter, instagram, facebook):
        self.nome = nome
        self.telefone = telefone
        self.email = email
        self.twitter = twitter
        self.instagram = instagram
        self.facebook = facebook


def abrir_arquivo() -> list:
    contatos = []

    try:
        with open('contatos.csv', 'r') as f:
            leitor = DictReader(f)
            for linha in leitor:
                contato = Contato(linha['nome'], linha['telefone'], linha['email'], linha['twitter'],
                                  linha['instagram'], linha['facebook'])
                contatos.append(contato.__dict__)
        return contatos
    except IOError:
        return contatos


def salvar_arquivo(contatos: list):
    with open("contatos.csv", "w+", newline='') as f:
        f.seek(0)
        f.write("nome,telefone,email,twitter,instagram,facebook\n")
        for contato in contatos:
            f.write(
                f'{contato["nome"]},{contato["telefone"]},{contato["email"]},{contato["twitter"]},'
                f'{contato["instagram"]}, {contato["facebook"]}\n')


def imprimir_tabela(tabela: list):
    t = PrettyTable(["Nome", 'Telefone', 'E-mail', 'Twitter', 'Instagram', 'Facebook'])
    for i in tabela:
        t.add_row(i)
    print(t)


def editar_contato(contatos: list) -> bool:
    nome = input("Digite o nome: ")
    for contato in contatos:
        if contato['nome'] == nome:
            tabela = [[contato['nome'], contato['telefone'], contato['email'], contato['twitter'], contato['instagram'],
                       contato['facebook']]]
            imprimir_tabela(tabela)

            contato['nome'] = input("Digite o novo nome: ")
            contato["telefone"] = input("Digite o novo telefone: ")
            contato['email'] = input("Digite o novo e-mail: ")
            contato['twitter'] = input("Digite o novo twitter: ")
            contato['instagram'] = input("Digite o novo instagram: ")
            contato['facebook'] = input("Digite o novo facebook: ")

            tabela = [[contato['nome'], contato['telefone'], contato['email'], contato['twitter'],
                       contato['instagram'], contato['facebook']], ]
            imprimir_tabela(tabela)
            return True
    print("Nenhum contato com esse nome.\n")
    return False


def listar_contatos(contatos: list):
    tabela = []
    for contato in contatos:
        tabela.append([contato['nome'], contato['telefone'], contato['email'], contato['twitter'],
                       contato['instagram'], contato['facebook']])

    imprimir_tabela(tabela)


def excluir_contato(contatos: list) -> bool:
    nome = input("Digite o nome: ")
    for contato in contatos:
        if contato['nome'] == nome:
            contatos.remove(contato)
            print("Contato removido\n")
            return True
    print("Nenhum contato com esse nome\n")
    return False


def gravar_dados() -> dict:
    nome = input("Digite o nome: ")
    telefone = input("Digite o telefone: ")
    email = input("Digite o e-mail: ")
    twitter = input("Digite o twitter: ")
    instagram = input("Digite o instagram: ")
    facebook = input("Digite o facebook: ")
    return {'nome': nome, 'telefone': telefone, 'email': email, 'twitter': twitter, 'instagram': instagram,
            'facebook': facebook}


def consultar_contato(contatos: list):
    nome = input("Digite o nome: ")
    is_contained = False
    tabela = []
    for contato in contatos:
        if contato['nome'] == nome:
            is_contained = True
            tabela = [[contato['nome'], contato['telefone'], contato['email'], contato['twitter'],
                       contato['instagram'], contato['facebook']]]
    if is_contained:
        imprimir_tabela(tabela)
    else:
        print("Nenhum contato com este nome.\n")


def imprimir_menu():
    print("\n\nDigite:")
    print("1 para inserir um novo contato;")
    print("2 para fazer uma consulta;")
    print("3 para remover um contato;")
    print("4 para editar um contato;")
    print("5 para listar todos os contatos;")
    print("6 para sair.")


def conferir_entrada(entrada: int, contatos: list):
    if entrada == 1:

        contatos.append(gravar_dados())
    elif entrada == 2:
        consultar_contato(contatos)
    elif entrada == 3:
        excluir_contato(contatos)
    elif entrada == 4:
        editar_contato(contatos)
    elif entrada == 5:
        listar_contatos(contatos)


def imprimir_saida_salvar():
    print("Deseja salvar os dados?")
    print("1 para sim;")
    print('2 para não.')


def conferir_saida_salvar(contatos: list):
    entrada = input()
    if entrada == '1':
        salvar_arquivo(contatos)
        print("Arquivo contatos.csv salvo.")


def menu_agenda():
    contatos = abrir_arquivo()
    listar_contatos(contatos)
    try:
        entrada = 0
        while entrada != 6:
            imprimir_menu()
            entrada = int(input())
            conferir_entrada(entrada, contatos)

        imprimir_saida_salvar()
        conferir_saida_salvar(contatos)
    except TypeError as e:
        print(e)
        print("Entrada inválida")


if __name__ == '__main__':
    menu_agenda()
