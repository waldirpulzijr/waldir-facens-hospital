from entidades.pacientes import Paciente
from entidades.pacientes import ListarPaciente
from operacoes.pacientes import OperacoesPaciente

class Initialize():

    def __init__(self):
        self.operacao_paciente = OperacoesPaciente()
        self.lista_pacientes = ListarPaciente()

    def load_classes(self):
        self.lista_pacientes = self.operacao_paciente.load() 

    def show_menu(self):
        print('\n')
        print(50 * '-')
        print('Bem-vindo ao Sistema Hospital - 2025!')
        print(50 * '-')

        print('1 - Pacientes')
        print('2 - Consultas')
        print('3 - Procedimentos')
        print('4 - Sair') 

    def choose_option(self):
        option = input('\nEscolha uma das opções: ')

        if option != '1' and option != '2' and option != '3' and option != '4':
            print('\nOpção inválida!')

        return option

    def show_sub_menu(self, option):
        print('\n') 
        print(50 * '-')
        if (option == '1'): 
            print('Pacientes:')
        elif (option == '2'):
            print('Consultas:')
        elif (option == '3'):
            print('Procedimentos:') 
        print(50 * '-')

        print('1 - Cadastrar')
        print('2 - Listar')
        print('3 - Excluir')
        print('4 - Voltar') 

    def choose_sub_option(self):
        sub_option = input('\nEscolha uma das opções: ')

        if sub_option != '1' and sub_option != '2' and sub_option != '3' and sub_option != '4':
            print('\nOpção inválida!')

        return sub_option
    
    def to_add(self, option):
        print('\n')

        if option == '1':
            nome = input('Informe o nome do paciente: ')
            cpf  = input('Informe o cpf do paciente: ')
            data_nasc = input('Informe a data de nascimento do paciente: ')

            count_lista_pacientes = len(self.lista_pacientes.listar()) + 1
            paciente = Paciente(count_lista_pacientes, nome, cpf, data_nasc)

            self.operacao_paciente.paciente = paciente
            self.operacao_paciente.save()
            init.load_classes()

    def to_listar(self, option):
        print('\n')

        if option == '1':
            for paciente in self.lista_pacientes.listar():
                print(f'Codigo: {paciente.codigo} - Nome: {paciente.nome} - CPF: {paciente.cpf} - Data de Nasc.: {paciente.data_nasc}')

    def to_excluir(self, option):
        print('\n')

        if option == '1':
            codigo = input('Informe o codigo do paciente a ser excluido: ')
            self.operacao_paciente.excluir(codigo)
            init.load_classes()

    def to_go_out(self):
        print('\nObrigado, volte sempre!')

if __name__ == "__main__":
    init = Initialize()
    init.load_classes()
    option = ''

    while option != '4':
        init.show_menu()
        option = init.choose_option()

        if option in ('1','2','3'):
            sub_option = ''

            while sub_option != '4':
                init.show_sub_menu(option)
                sub_option = init.choose_sub_option()

                if sub_option == '1': ### Cadastrar
                    init.to_add(option)

                elif sub_option == '2': ### Listar
                    init.to_listar(option)

                elif sub_option == '3': ### Excluir
                    init.to_excluir(option)

        elif option == '4':
            init.to_go_out()
