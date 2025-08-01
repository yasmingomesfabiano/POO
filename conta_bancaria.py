class Conta_bancaria:
    def __init__(self,titular,saldo_inicial=0):
        self.__titular=titular
        self.__saldo=saldo_inicial
    #metodo publico para depositar   
    def depositar(self,valor):
        if valor >0:
            self.__saldo += valor 
            print(f'Depósito de R${valor} realizado com sucesso!')
        else:
            print('Valor de depósito inválido.')
    #metodo publico para sacar        
    def sacar(self,valor):
        if 0 <= self.__saldo:
            self.__saldo -= valor
            print(f'Saque de R${valor} realizado com sucesso!')
        else:
            print('Saldo insuficiente ou valor inválido para saque.')
    #metoo publico para consultar o saldo
    def consultar_saldo(self):
        return self.__saldo
    
    '''Getter|Setter
    Getter= é um método usado para obter(ler) o valor de um atributo privado
    de uma classe
    Setter=é usado para definir (escrever) ou alterar o valor de um atributo
    privado de uma classe'''
    
    #Getter para o titular(somente leitura)
    @property #getter-cria um método que pode ser acessado como se fosse um atributo
    def titular(self):
        return self.__titular
    
#usar classe

conta=Conta_bancaria('João Silva',1000)
print(conta.titular) #saída: João silva
print(conta.consultar_saldo()) #saída: 1000

conta.depositar(500) #depósito
print(conta.consultar_saldo())

conta.sacar(200)
print(conta.consultar_saldo())
print(conta.__saldo)
