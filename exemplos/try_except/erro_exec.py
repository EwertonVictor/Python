try:
    x = int(input("Digite um número: "))
    y = int(input("Digite outro número: "))
    if y == 0:
        raise RuntimeError("Divisão por zero não é permitida.")
    resultado = x / y
    print(f"O resultado é: {resultado}")
except RuntimeError as e:
    print(f"Erro de execução: {e}")
except ValueError:
    print("Erro: Entrada inválida! Por favor, digite um número.")
