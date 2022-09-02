from modelNovo import modelNovo

class control:
    def __init__(self):
        self.opcao = -1
        self.modelo = modelNovo()

    def getOpcao(self):
        return self.opcao

    def setOpcao(self, opcao):
        self.opcao = opcao

    def menu(self):
        print("Escolha uma das opções anaixo: \n"  +
              "\n0. Sair"                          +
              "\n1. Cadastrar"                     +
              "\n2. Consultar"                     +
              "\n3. Atualizar Nome"                +
              "\n5. Atualizar Endereço"            +
              "\n6. Atualizar Telefone"            +
              "\n7. Atualizar Data De Nascimento"                +
              "\n8  Atualizar E-Mail"               +
              "\n9. Atualizar CID"                  +
              "\n10. Atualizar Salário"                 +
              "\n11. Excluir")
        self.setOpcao(int(input()))

    def operacoes(self):
        while self.getOpcao() != 0:
            self.menu()
            if self.getOpcao() == 0:
                print("Obrigado!")
            elif self.getOpcao() == 1:
                self.cadastrar()
            elif self.getOpcao() == 2:
                print(self.modelo.selecionar())
            elif self.getOpcao() == 3:
                self.atualizarNome()
            elif self.getOpcao() == 4:
                self.atualizarEndereco()
            elif self.getOpcao() == 5:
                self.atualizarEndereco()
            elif self.getOpcao() == 6:
                self.atualizarTelefone()
            elif self.getOpcao() == 7:
                self.atualizarData()
            elif self.getOpcao() == 8:
                self.atualizarEmail()
            elif self.getOpcao() == 9:
                self.atualizarCID()
            elif self.getOpcao() == 10:
                self.atualizarSalario()
            elif self.getOpcao() == 11:
                self.excluir()


                print("Opção escolhida invalinda! Tente novamente!")


    def cadastrar(self):
        print("informe o ser nome: ")
        nome = input()
        print("Informe seu telefone: ")
        telefone = input()
        print("informe seu endereço ")
        endereco = input()
        print("Informe seu email")
        email = input()
        print("Informe o CID")
        CID = input()
        print("Informe o salário")
        salario = input()
        print("Informe a sua data de nascimento: ")
        dataDeNascimento = input()
        print(self.modelo.inserir(nome, telefone, endereco, email, CID, salario, self.transformarData(dataDeNascimento)))

    def transformarData(self, texto):
        separado = texto.split('/')
        dia = separado[0]
        mes = separado[1]
        ano = separado[2]
        return "{}-{}-{}".format(ano, mes, dia)

    def atualizarNome(self):
        print("Informe o codigo do dado que sera atualizado!")
        codigo = int(input())
        print("Informe o novo nome")
        nome = input()
        print(self.modelo.atualizar("nome", nome, codigo))

    def atualizarTelefone(self):
        print("Informe o codigo do dado que sera atualizado!")
        codigo = int(input())
        print("Informe o novo telefone")
        tel = input()
        print(self.modelo.atualizar("telefone", tel, codigo))


    def atualizarEndereco(self):
        print("Informe o codigo do dado que sera atualizado!")
        codigo = int(input())
        print("Informe o novo enedereco")
        end = input()
        print(self.modelo.atualizar("endereco", end, codigo))


    def atualizarData(self):
        print("Informe o codigo do dado que sera atualizado!")
        codigo = int(input())
        print("Informe o novo data")
        data = self.transformarData(input())
        print(self.modelo.atualizar("dataDeNascimento", data, codigo))

    def atualizarEmail(self):
        print("Informe o codigo do dado que sera atualizado!")
        codigo = int(input())
        print("Informe o novo E-mail")
        email = input()
        print(self.modelo.atualizar("email", email, codigo))

    def atualizarCID(self):
        print("Informe o codigo do dado que sera atualizado!")
        codigo = int(input())
        print("Informe o novo CID")
        cid = input()
        print(self.modelo.atualizar("CID", cid, codigo))

    def atualizarSalario(self):
        print("Informe o codigo do dado que sera atualizado!")
        codigo = int(input())
        print("Informe o novo salário")
        sal = input()
        print(self.modelo.atualizar("salario", sal, codigo))

    def excluir(self):
        print("informe o codigo do dado que deseja excluir:")
        cod = int(input())
        print(self.modelo.excluir(cod))






