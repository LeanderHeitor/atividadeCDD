class Pessoa():
    def __init__(self, nome,peso,idade,comendo=False,falando=False):#atributos
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.comendo=False
        self.falando=False
    def comer(self,alimento):#metodos4
        if self.falando == True:
            print(f"{self.nome} está falando, logo, não pode comer")
        if self.comendo == False:
            print(f"{self.nome} está comendo {alimento}")
            self.comendo = True
        else:
            print(f"{self.nome} já está comendo")
    def pararDeComer(self,alimento):#metodos
        if self.comendo == True:
            print(f"{self.nome} terminou de comer {alimento}")
            self.comendo = False
        else:
            print(f"{self.nome} já não está comendo nada")
        self.comendo = False
    def falar(self, falas):#metodos
        if self.falando == False:
            print(f"{self.nome} está falando que: {falas}")
            self.falando == True
        else:
            print(f"{self.nome} já está falando")
    def andar(self,km):#metodos
        print(f"{self.nome} vai andar {km}km")
class ContaBancaria():
    def __init__(self,numConta,nomeCliente,tipoConta,):
        self.numConta = numConta
        self.saldo = 0
        self.nomeCliente = nomeCliente
        self.tipoConta = tipoConta
        self.status = False
    def mostrarSaldo(self):
        if self.status == True:
            print(f"{self.nomeCliente} seu saldo é de {self.saldo}R$")
        else:
            print(f"conta inativa")
    def ativarConta(self):
        if self.status == False:
            print(f"{self.nomeCliente} sua conta acabou de ser ativada")
            self.status = True
        else:
            print(f"a conta de {self.nomeCliente} já está ativa")
    def desativarConta(self):
        if self.status == True:
            if self.saldo > 0:
                print(f"{self.nomeCliente} sua conta possui saldo, saque-o para desativa-lá")
            else:
                print(f"{self.nomeCliente} sua conta acabou de ser desativada :/")
                self.status = False
        else:
            print(f"a conta de {self.nomeCliente} já está desativada")
    def depositar(self,valor):
        if self.status == True:
            self.saldo = self.saldo+valor
            print(f"{self.nomeCliente} você acabou de depositar {valor}R$ com sucesso!")
        else:
            print("conta inativa")
    def sacar(self,valor):
        if self.status == True:
            if self.saldo>0:
                if valor<=self.saldo:
                    print(f"{self.nomeCliente} você acabou de sacar {valor}R$ de sua conta")
                    self.saldo = self.saldo - valor
                else:
                    print(f"Não é possivel sacar {valor}R$, saldo insuficiente")
            else:
                print(f"{self.nomeCliente} sua conta está zerada")
        else:
            print("conta inativa")

class Animal():
    def __init__(self,nome,cor):
        self.nome=nome
        self.cor=cor
    def comer(self,sarro):
        print(f"{self.nome} foi comer {sarro}")
class Gato(Animal):
    def __init__(self,nome, cor):
        super().__init__(nome,cor)
    def miar(self):
        print(f"{self.nome} foi miar por ai, miau miau")

    def padeiro(self):
        print(f"{self.nome} está amassando pãozinho, a padaria está a todo vapor, que fofo!")
class Cachorro(Animal):
    def __init__(self,nome,cor):
        super().__init__(nome,cor)
    def latir(self):
        print(f"{self.nome} latiu... MUITO")

class Coelho(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def pular(self):
        print(f"{self.nome} pulou por ai... de forma indefinida")


class Vaca(Animal):
    def __init__(self, nome, cor):
        super().__init__(nome, cor)

    def mugir(self):
        print(f"{self.nome} mugiu...muuuh")
