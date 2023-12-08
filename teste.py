from pessoa import Pessoa
from aluno import Aluno
from professor import Professor

p = Pessoa('Marlon', '85', '1.78', 'Masculino', '25/06/1987')
a = Aluno('Marlon', '85', '1.78', 'Masculino', '25/06/1987')
a.set_matricula('3355')
pr = Professor('Marlon', '85', '1.78', 'Masculino', '25/06/1987')
pr.set_disciplina('Engenharia de Software')

print(p.get_nome())
print(p.obter_dados())
print('-'*50)
print(a.get_nome())
print(a.get_matricula())
print(a.obter_dados())
print('-'*50)
print(pr.get_nome())
print(pr.get_disciplina())
print(pr.obter_dados())
