class Pessoa:
    def __init__(self, nome=None, peso=None, altura=None, genero=None, data_nascimento=None):
        self.__nome = nome
        self.__peso = peso
        self.__altura = altura
        self.__genero = genero
        self.__data_nascimento = data_nascimento

    def obter_dados(self):
        return f'Nome: {self.__nome} - Peso: {self.__peso} - Altura: {self.__altura} - Gênero: {self.__genero} - Data Nascimento: {self.__data_nascimento}'
    
    #getters
    def get_nome(self):
        return self.__nome
    
    def get_peso(self):
        return self.__peso
    
    def get_altura(self):
        return self.__altura
    
    def get_genero(self):
        return self.__genero
    
    def get_data_nascimento(self):
        return self.__data_nascimento
    
    #setters
    def set_nome(self, nome):
        self.__nome = nome

    def set_peso(self, peso):
        self.__peso = peso

    def set_altura(self, altura):
        self.__altura = altura

    def set_genero(self, genero):
        self.__genero = genero

    def set_data_nascimento(self, data_nascimento):
        self.__data_nascimento = data_nascimento