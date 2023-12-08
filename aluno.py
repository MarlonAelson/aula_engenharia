from pessoa import Pessoa

class Aluno(Pessoa):
    def __init__(self, nome=None, peso=None, altura=None, genero=None, data_nascimento=None, matricula=None):
        super().__init__(nome, peso, altura, genero, data_nascimento)
        self.__matricula = matricula

    def obter_dados(self):
        return super().obter_dados() + ' - Matricula:  ' + self.__matricula
    
    def get_matricula(self):
        return self.__matricula
    
    def set_matricula(self, matricula):
        self.__matricula = matricula
    
        #return f'Nome: {self.__nome} - Peso: {self.__peso} - Altura: {self.__altura} - Gênero: {self.__genero} - Data Nascimento: {self.__data_nascimento}'