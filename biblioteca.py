'''Crie um programa em Python que simule um sistema simples de biblioteca
utilizando conceitos de Programação Orientada a Objetos (POO). O sistema deve:
Definir uma classe Livro que contenha, pelo menos, os atributos:

    titulo (nome do livro)

    autor (nome do autor)

Criar uma lista com pelo menos 10 objetos Livro, representando os livros disponíveis 
na biblioteca.
Solicitar ao usuário o nome do solicitante do empréstimo.
Exibir a lista de livros disponíveis, numerada para facilitar a seleção.
Pedir para o usuário escolher um número correspondente ao livro que deseja pegar 
emprestado.
Imprimir uma mensagem confirmando o empréstimo, informando o nome do
solicitante e o livro selecionado (título e autor).'''

#Criando a class
class Livro:
    def __init__(self,titulo,autor):
        self.titulo=titulo
        self.autor=autor
    
#Lista 
    def mostrar_autor(self,numero):
        return f'{numero}) livro: {self.titulo}\n   autor:{self.autor}.'
    
livro1=Livro('Dom Casmurro', 'Machado de Assis')
livro2=Livro('1984', 'George Orwell')
livro3=Livro('O pequeno Príncipe', 'Antoine de Saint')
livro4=Livro('A Menina que Roubava Livros', 'Markus Zusak')
livro5=Livro('Harry Potter e a Pedra Filosofal ', ' J.K. Rowling ')
livro6=Livro('O Código Da Vinci', 'Dan Brown')
livro7=Livro('Capitães da Areia', 'Jorge Amado')
livro8=Livro('O Hobbit', 'J.R.R. Tolkien')
livro9=Livro('Torto Arado', 'Itamar Vieira Junior ')
livro10=Livro('Ensaio sobre a Cegueira', 'José Saramago')

livros=[livro1,livro2,livro3,livro4,livro5,livro6,livro7,livro8,livro9,livro10]
for i, livro in enumerate(livros):  
    print(livro.mostrar_autor(i + 1))
         
#pedir para o usuario o numero(usar o switch)
nome = input("\nDigite seu nome para realizar o empréstimo: ")
escolha=int(input("Digite o número do livro:"))  
if escolha < 1 or escolha > 10:
    print("Número inválido! O programa será encerrado.")
    exit()

def livro_emprestado(numero):
    match numero:
        case 1:
            return livro1
        case 2:
            return livro2
        case 3:
            return livro3
        case 4:
            return livro4
        case 5:
            return livro5
        case 6:
            return livro6
        case 7:
            return livro7
        case 8:
            return livro8
        case 9:
            return livro9
        case 10:
            return livro10
        case _:
            return None
livro_escolhido=livro_emprestado(escolha)
print(f"Empréstimo realizado com sucesso!")
print(f"Solicitante: {nome}")
print(f"Livro emprestado: '{livro_escolhido.titulo}' de {livro_escolhido.autor}")



'''correção da professora:
class Livro:
    def __init__(self,titulo,autor):
        self.titulo=titulo
        self.autor=autor
    
def main()
    livros=[
        livro=Livro('Dom Casmurro', 'Machado de Assis')
        livro=Livro('1984', 'George Orwell')
        livro=Livro('O pequeno Príncipe', 'Antoine de Saint')
        livro=Livro('A Menina que Roubava Livros', 'Markus Zusak')
        livro=Livro('Harry Potter e a Pedra Filosofal ', ' J.K. Rowling ')
        livro=Livro('O Código Da Vinci', 'Dan Brown')
        livro=Livro('Capitães da Areia', 'Jorge Amado')
        livro=Livro('O Hobbit', 'J.R.R. Tolkien')
        livro=Livro('Torto Arado', 'Itamar Vieira Junior ')
        livro=Livro('Ensaio sobre a Cegueira', 'José Saramago')
        
    ]
nome=input('Digite seu nome:')
print('\n Livros disponiveis para empréstimo: )
for i, livro in enumerate(livros, start=1):
  print(f'{i}.{livro.titulo}-{livro.autor}')
  
while True:
    escolha= int(input(\n Digite o núumero do livro que deseja pegar emprestado:))
    
    if 1 <= escolha <= len(livros):
        livro_selecionado=livros[escolha -1]
        break
    else:
        print(f'por favor, digite um número entre 1 e {len(livros)}')
    print(f'\n Empréstimo confirmado!')
    print(f'{nome}pegou emprestado o livro 'livro_selecionado.titulo' de {livro_selecionado.autor}.
main()'''
    

