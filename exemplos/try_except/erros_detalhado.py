try:
    x = int(input('Digite um valor: '))
    y = int(input('Digite outro valor: '))
    soma = x + y
    print(f'\nSoma: {soma}')
except Exception as e:
    print(f'Ocorreu um erro: {e}')
