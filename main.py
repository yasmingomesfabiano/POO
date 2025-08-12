from aluno import Aluno #from= nome do arquivo import=nome da class 

def main():
    print('cadastro do aluno:')
    nome=('nome: ')
    matricula= input('matricula: ')
    curso= input('curso: ')
    
    
    disciplinas= []
    notas= []
    
    print('informe 3 disciplinas e as notas correspondentes: ')
    for i in range(3):
        disciplina= input(f'nome da disciplina {i+1}: ')
        
    while True:
        try:
            nota=float(input(f'nota da disciplina {disciplina}:'))
            if 0 <=nota <= 10:
                break
            else:
                print('a nota deve ser entre 0 e 10.')
        except ValueError:
            print('digite uma nora válida(número).')
            
    