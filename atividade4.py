#region EXIGÊNCIA DE CÓDIGO 1 de 8
print("Bem-vindos à empresa do Gustavo de Jesus de Oliveira")  
#endregion

#region Lista de funcionários e ID global
lista_funcionarios = []
id_global = 4731222  # RU [EXIGÊNCIA DE CÓDIGO 2 de 8]
#endregion

#region Menus
_menuPrincipal = """
 ----------------------------------
-----------MENU PRINCIPAL-----------
|   1. Cadastrar Funcionário       |
|   2. Consultar Funcionários      | 
|   3. Remover Funcionário         |        
|   4. Sair                        |    
------------------------------------
"""
_menuConsultaFuncionario = """
 ----------------------------------
------------OPÇÕES DE CONSULTA------------
|   1. Consultar Todos os Funcionários   |
|   2. Consultar Funcionário por Id      | 
|   3. Consultar Funcionário(s) por Setor |        
|   4. Retornar                          |    
------------------------------------------
"""
_menuRemoverFuncionario ="""------MENU REMOVER FUNCIONÁRIO------"""


def _menuInfoFuncionario(funcionario):


    print("""
    ----------------------------------
    ID: {id}
    Nome: {nome}
    Setor: {setor}
    Salário: R$ {salario:.1f}
    ----------------------------------
    """.format(id=funcionario['id'], nome=funcionario['nome'], setor=funcionario['setor'], salario=funcionario['salario']))


#endregion

#region Função para cadastrar funcionário
def cadastrar_funcionario(id):
    
    idInfo = "Id do funcionario: {id}".format( id=id)

    while True:
        print(idInfo)
        nome = input("Por favor, entre com o nome do funcionário: ").strip()
        setor = input("Por favor, entre com o setor do funcionário: ").strip()
        
        try:
            salario = float(input("Por favor, entre com o salário do funcionário: ").strip())
            if salario <= 0:
                print("O salario deve ser um valor positivo. Tente novamente.")
                continue
        except ValueError:
            print("Valor invalido. Por favor, entre com um numero valido para o salario.")
            continue
        
        # sair do loop
        break
    
    # criaçao do dicionario do funcionrio, objeto?
    funcionario = {
        'id': id,
        'nome': nome,
        'setor': setor,
        'salario': salario
    }
    
    # adicionando o dicionario a lista de funcionarios
    lista_funcionarios.append(funcionario.copy())
    #print(f"Funcionário {nome} cadastrado com sucesso!")
#endregion

#region função para consultar funcionários
def consultar_funcionarios():
    while True:
        print(_menuConsultaFuncionario)
        opcao = input(">> ")
        
        if opcao == "1":
            # consultar todos os funcionarios
            print("\nLista de Todos os Funcionários:")
            for funcionario in lista_funcionarios:
                 _menuInfoFuncionario(funcionario)
        
        elif opcao == "2":
            # consultar funcionario por ID
            idd = int(input("Digite o ID do funcionário: "))
            encontrado = False
            for funcionario in lista_funcionarios:
                if funcionario["id"] == idd:
                    _menuInfoFuncionario(funcionario)
                    encontrado = True
                    break
            if not encontrado:
                print("Funcionário não encontrado.")
        
        elif opcao == "3":
            # consultar funcionario por setor
            setor_consulta = input("Digite o setor do(s) funcionário(s): ")
            encontrado = False
            for funcionario in lista_funcionarios:
                if funcionario["setor"].lower() == setor_consulta.lower():
                    _menuInfoFuncionario(funcionario)
                    encontrado = True
            if not encontrado:
                print("Nenhum funcionário encontrado nesse setor.")
        
        elif opcao == "4":
            # retornar ao menu principal
            return
        
        else:
            print("Opção inválida. Tente novamente.")
#endregion

#region funcão para remover funcionario
def remover_funcionario():
    while True:
        print(_menuRemoverFuncionario)
        idd = int(input("Digite o ID do funcionário a ser removido: "))
        encontrado = False
        for i, funcionario in enumerate(lista_funcionarios):
            if funcionario["id"] == idd:
                del lista_funcionarios[i]
                print("Funcionário removido com sucesso!")
                encontrado = True
                break
        if not encontrado:
            print("Id inválido. Tente novamente.")
        else:
            break
#endregion

#region Main 
while True:
    print(_menuPrincipal)
    opcao = input("> ")
  
    if opcao == "1":
        id_global += 1  # incrementa o id_global
        cadastrar_funcionario(id_global)
    
    elif opcao == "2":
        consultar_funcionarios()
    
    elif opcao == "3":
        remover_funcionario()
    
    elif opcao == "4":
        print("Saindo do sistema...")
        break
    
    else:
        print("Opção inválida. Tente novamente.")
#endregion


