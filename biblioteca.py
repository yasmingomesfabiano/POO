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
        return f'{numero}livro:{self.titulo}\n   autor:{self.autor}.'
    
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
