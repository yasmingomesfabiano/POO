'''class Aluno:
    def __init__(self, nome, matricula, curso, disciplina,notas):
        self.nome=nome
        self.matricula=matricula
        self.curso=curso
        self.disciplina=[]
        self.notas=[]
               
nome=input('digite seu nome: ')
matricula=int(input('informe sua matricula: '))

print(f'aluno: {nome}\nnúmero da matricula: {matricula}') 
print(f'matriculado no curso: matemática')

for i in range(3): 
    disciplina = input(f'Digite o nome da disciplina {i+1}: ')

for i in range(3): 
    notas= float(input(f'Digite sua nota {i+1}: '))
      
def mostrar_nota(notas):    
    if notas >= 7 < 10:
        return 'Aprovado!'
    else:
        return 'Reprovado!'
    
print(f'aluno:{nome}\nnúmero da matrícula:{matricula}\n{self.diciplina[]}\n{self.notas[]}') #erro!'''

class Aluno:
    def __init__(self, nome, matricula, curso, disciplinas,notas):
          self.nome=nome
          self.matricula=matricula
          self.curso=curso
          self.disciplinas=disciplinas
          self.notas=notas 
    
    def verifica_aprovacao(self,disciplina):
        #verificar se a diciplina está na lista 
        if disciplina in self.disciplinas:
            indice= self.disciplinas.index(disciplina)
            return self.notas[indice] >=7
        
        else:
            print(f'Disciplina "{disciplina}" não encontrada.')
        
    

    
        

        



    