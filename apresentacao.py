#Definir a classe Pessoa
class Pessoa:
    def __init__(self, nome, idade): #construtor: inicializa atributos ao criar objetos(__init__)
        self.nome=nome #atributo nome #instância atual da classe = o objeo que está executando o método
        self.idade=idade #atributo idade
        
    def apresentar(self):
       print(f'olá meu nome é {self.nome} e tenho {self.idade} anos.')

#criando objetos

pessoa1=Pessoa('Ana',25)
pessoa2=Pessoa('Thais',27)
pessoa3=Pessoa('Fernando',18)

#usando objetos
pessoa1.apresentar()
pessoa2.apresentar()
pessoa3.apresentar()
