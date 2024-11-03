#Criar classe "Conta Bancária"
class ContaBancaria:
    def __init__(self, titluar='', saldo=0, ativo=False):
        self.titular = titluar
        self.saldo = saldo
        self._ativo = False

    def __str__(self):
        return f'Titular: {self.titular}\nSaldo: {self.saldo}'
    
    @classmethod
    def ativar_conta(cls, conta):
        conta._ativo = True
    
#Instanciar classes
conta1 = ContaBancaria('Ewerton', 1000)

#Imprimir as instâncias
print(f'Antes de ativar: Conta ativa? {conta1._ativo}')
ContaBancaria.ativar_conta(conta1)
print(f'Depois de ativar: Conta ativa? {conta1._ativo}')