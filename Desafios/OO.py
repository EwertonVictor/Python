class Pessoa:
    def __init__(self, nome='', idade=0, profissao=''):
        self.nome = nome
        self.idade = idade
        self.profissao = profissao
    
    def __str__(self):
        return f'Nome: {self.nome}\nIdade: {self.idade} Anos\nProfissão: {self.profissao}'

    @property
    def saudacao(self):
        if self.profissao:
            return f'Olá, sou {self.nome}! Trabalho como {self.profissao}'
        else:
            return f'Olá sou {self.nome}!'

    def aniversario(self):
        self.idade += 1

pessoa1 = Pessoa('Ewerton',25,'Analista de Service Desk')

print('Informações Inciais:\n')
print(pessoa1)
print()