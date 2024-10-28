def somar_dois_valores():
    try:
        x = int(input('Digite um valor: '))
        y = int(input('Digite outro valor: '))
        soma = x + y
        return soma
    except ValueError:
        print('Valor inválido! Por favor, digite um número inteiro.')


resultado = somar_dois_valores()
print(f'\nResultado é: {resultado}')
