from pessoa import Pessoa

class Professor(Pessoa):
    def __init__(self, nome=None, peso=None, altura=None, genero=None, data_nascimento=None, disciplina=None):
        super().__init__(nome, peso, altura, genero, data_nascimento)
        self.__disciplina = disciplina

    def obter_dados(self):
        return super().obter_dados() + ' - Disciplina:  ' + self.__disciplina
    
    def get_disciplina(self):
        return self.__disciplina
    
    def set_disciplina(self, disciplina):
        self.__disciplina = disciplina
    
        #return f'Nome: {self.__nome} - Peso: {self.__peso} - Altura: {self.__altura} - Gênero: {self.__genero} - Data Nascimento: {self.__data_nascimento}'