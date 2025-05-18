import csv
import os.path

from configs.configs import Configuracoes
from datetime import date

class ProcessarPaciente():
    def __init__(self):
        self.__configurations = Configuracoes()

    def read_file(self):
        if os.path.isfile(self.__configurations.file_pacientes):
            with open(self.__configurations.file_pacientes, 'r') as arquivo:
                arquivo_csv = csv.reader(arquivo, delimiter=',')
                return list(arquivo_csv)
        else:
            return []    
        
    def wrote_file(self, paciente):
        registro_paciente = [paciente.codigo, paciente.nome, paciente.cpf, paciente.data_nasc]
        with open(self.__configurations.file_pacientes, 'a', newline='', encoding='UTF-8') as arquivo:
            escritor = csv.writer(arquivo, delimiter=',')
            escritor.writerow(registro_paciente)

    def filter_file(self, codigo):
        lista = self.read_file() 
        with open(self.__configurations.file_pacientes, 'w', newline='', encoding='UTF-8') as arquivo:
            escritor = csv.writer(arquivo, delimiter=',')
            for paciente in lista:
                if paciente[0] != codigo:
                    escritor.writerow(paciente)
