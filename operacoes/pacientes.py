from entidades.pacientes import Paciente
from entidades.pacientes import ListarPaciente
from processar.pacientes import ProcessarPaciente

class OperacoesPaciente():
    def __init__(self, paciente=None):
        self.__processar = ProcessarPaciente()
        self.__paciente = paciente

    @property ## Equivale ao GET
    def paciente(self):
        return self.__paciente

    @paciente.setter ## Equivale ao SET
    def paciente(self, paciente):
        self.__paciente = paciente

    def load(self):
        lista = self.__processar.read_file()
        lista_pacientes = ListarPaciente()

        for linha in lista:
            paciente = Paciente(linha[0], linha[1], linha[2], linha[3])
            lista_pacientes.inserir(paciente)

        return lista_pacientes    

    def save(self):
        self.__processar.wrote_file(
            self.__paciente
        )

    def excluir(self, codigo):
        self.__processar.filter_file(
            codigo
        )
