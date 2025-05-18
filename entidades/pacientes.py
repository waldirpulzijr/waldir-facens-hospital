

class Paciente():
  def __init__(self, codigo, nome, cpf, data_nasc):
    self.codigo = codigo
    self.nome = nome
    self.cpf = cpf
    self.data_nasc = data_nasc

class ListarPaciente():
  def __init__(self):
    self.lista = []

  def inserir(self, paciente):
    self.lista.append(paciente)

  def listar(self):
    return self.lista 
