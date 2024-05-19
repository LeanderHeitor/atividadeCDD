class Pessoa():
    def __init__(self,nome,peso,idade,comendo,falando,correndo):
        self.nome=nome
        self.peso=peso
        self.idade=idade
        self.comendo = False
        self.falando = False
        self.correndo = False

    def comer(self, comida):
        if self.falando == True:
            print(f"{self.nome} está falando.")
        elif self.correndo == True:
            print(f"{self.nome} está correndo.")
        elif self.comendo == True:
            print(f"{self.nome} já está comendo.")
        else:
            print(f"{self.nome} foi comer {comida}.")
            self.comendo = True

    def falar(self, frase):
        if self.comendo == True:
            print(f"{self.nome} está comendo.")
        elif self.correndo == True:
            print(f"{self.nome} está correndo.")
        elif self.falando == True:
            print(f"{self.nome} já está falando.")
        else:
            print(f"{self.nome} disse '{frase}'")
            self.falando = True

    def correr(self):
        if self.comendo == True:
            print(f"{self.nome} está comendo.")
        elif self.falando == True:
            print(f"{self.nome} está falando.")
        elif self.correndo == True:
            print(f"{self.nome} já está correndo.")
        else:
            print(f"{self.nome} vai correr ")
            self.correndo = True

    def pararcorrer(self):
        if self.correndo == False:
            print(f"{self.nome} não está correndo.")
        else:
            print(f"{self.nome} parou de correr.")
            self.correndo = False

    def pararFalar(self):
        if self.falando == False:
            print(f"{self.nome} não está falando.")
        else:
            print(f"{self.nome} se calou.")
            self.falando = False

    def pararComer(self):
        if self.comendo == False:
            print(f"{self.nome} não está comendo.")
        else:
            print(f"{self.nome} fechou a boca.")
            self.comendo = False



