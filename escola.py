from abc import ABC, abstractmethod 
#curso no geral
class Curso(ABC):
    def __init__(self,nome):
        self.nome=nome
        self.alunos=[]
        
    def inscrever_alunos(self,aluno):
        self.alunos.append(aluno)
        print(f'Aluno {aluno} inscrito no curso {self.nome}.')
        
    @abstractmethod
    def info_curso(self):
        pass
#Curso especifico    
class CursoMatematica(Curso):
        def info_curso(self):
            print(f'Curso de {self.nome}: Foco em álgebra e geometria.')
            
#curso especifico
class CursoHistoria(Curso):
        def info_curso(self):
            print(f'Curso de {self.nome}: Foco em história mundial e cultura.')
            
#testar

curso1= CursoMatematica('Matemática')
curso2= CursoHistoria('História')

curso1.inscrever_alunos('Breno')
curso1.inscrever_alunos('Rayssa')
curso1.info_curso()

curso2.inscrever_alunos('Agatha')
curso2.info_curso()




