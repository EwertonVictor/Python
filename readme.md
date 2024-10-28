## O que são Exceptions em Python?
Exceptions em Python são erros que ocorrem durante a execução de um programa, sendo usadas para sinalizar situações excepcionais que podem interromper o fluxo normal do código. A principal forma de tratar esses erros é utilizando os blocos `try except`.

## [Exceptions comuns](./exemplos/try_except/excep_comum.py "Verifique o script do exemplo")
```ValueError:``` ocorre quando uma função recebe um argumento com o tipo certo, mas com o valor errado.
### Exemplo
```
x = int('Hello world!')
```
Neste exemplo, passamos o valor de uma `String` para um inteiro, o que gera o valor `ValueError`. 
```
ValueError: invalid literal for int() with base 10: 'Hello world!'
```
## [Try except](./exemplos/try_except/erros.py "Verifique o script do exemplo")
Em Python, uma das formas mais eficazes de tratar esses erros é utilizando o bloco `Try` e `Except`.
### Exemplo:
```
def somar_dois_valores():
    try:
        x = int(input('Digite um valor: '))
        y = int(input('Digite outro valor: '))
        soma = x + y
        return soma
    except ValueError:
        print('Valor inválido! Por favor, digite um número inteiro.')
```
O bloco `try` permite que você “tente” executar um bloco de código e, caso ocorra um erro, “capture” essa exceção e execute um código alternativo. o `except ValueError` captura essa exceção e exibe uma mensagem de erro apropriada.

##  [Exception as](./exemplos/try_except/erros_detalhado.py "Verifique o script do exemplo")
Para mostrar detalhes específicos do erro, podemos usar a sintaxe except Exception as. Isso nos permite capturar a exceção em uma variável e exibir informações detalhadas
### Exemplo
```
try:
    x = int(input('Digite um valor: '))
    y = int(input('Digite outro valor: '))
    soma = x + y
    print(f'\nSoma: {soma}')
except Exception as e:
    print(f'Ocorreu um erro: {e}')

```
Isso nos retornará a seguinte resposta: 

```
Ocorreu um erro: invalid literal for int() with base 10: 'a'
```
Qualquer exceção que ocorra dentro do bloco `try` será capturada pelo `except Exception as e`, e a mensagem de erro será armazenada na variável `e`
## O que é raise?
`raise` é útil para garantir que erros críticos sejam tratados imediatamente. Isso é especialmente importante em situações onde continuar a execução do código poderia levar a resultados incorretos ou danificar dados.\
__Veremos mais sobre isso no tópico abaixo.__
## [RuntimeError](./exemplos/try_except/erro_exec.py "Verifique o script do exemplo")
O `RuntimeError` é uma exceção genérica que pode ser usada para capturar erros que ocorrem durante a execução do programa. Podemos usá-lo para capturar e exibir mensagens de erro específicas
### Exemplo
```
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

```
Usamos `raise RuntimeError` para lançar uma exceção personalizada quando tenta dividir por zero. O `except RuntimeError as e` captura essa exceção e exibe a mensagem de erro personalizada.

Isso nos retornará a seguinte resposta:
```
Erro de execução: Divisão por zero não é permitida.
```
## [Try except else](./exemplos/try_except/erros_else.py "Verifique o script do exemplo")
O bloco `else` é executado apenas se o bloco `try` não gerar nenhuma exceção. Isso é útil para separar o código que deve ser executado apenas quando não há erros.
### Exemplo
```
try:
    x = int(input("Digite um número: "))
    y = int(input("Digite outro número: "))
    resultado = x / y
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero!")
except ValueError:
    print("Erro: Entrada inválida! Por favor, digite um número.")
else:
    print(f"O resultado é: {resultado}")
```
## [Try except else finally](./exemplos/try_except/else_finally.py "Verifique o script do exemplo")
O bloco `finally` é executado independentemente de qualquer exceção que ocorra. Isso é útil para liberar recursos ou executar ações de limpeza. Exemplo:
### Exemplo
```
try:
    x = int(input("Digite um número: "))
    y = int(input("Digite outro número: "))
    resultado = x / y
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero!")
except ValueError:
    print("Erro: Entrada inválida! Por favor, digite um número.")
else:
    print(f"O resultado é: {resultado}")
finally:
    print("Execução finalizada.")
```
O código que será executado independentemente de qualquer exceção.

## O que são Listas em Python
É uma estrutura de dados que armazena uma sequência de valores. As listas em Python são classificadas como um tipo de dado mutável, e portanto não possuem tamanho fixo: podemos adicionar ou remover elementos de listas de maneira dinâmica ao longo do código.
### Exemplo
```
minha_lista = [10, "Ewerton", 3.14, True, "Python"]
```
os valores não precisam ser do mesmo tipo de dado. Dentro de uma mesma lista, podemos misturar valores de diferentes tipos.
## [Acessando elemento em uma lista](./exemplos/Listas/indice.py "Verifique o script do exemplo")
Cada elemento dentro de uma lista possui um índice numérico partindo de zero.
### Exemplo
```
numeros = [1,2,3,4,5,6,7,8,9]
print(numeros[2])
```
Observando o exemplo acima, teremos como resultado o valor __3__. Conseguimos modificar a lista de forma semelhante.
### Exemplo
```
numeros = [1,2,3,4,5,6,7,8,9]
numeros[2] = 21
```
Saída do terminal: `[1,2,21,4,5,6,7,8,9]`
## [Append( )](./exemplos/Listas/adicionar.py "Verifique o script do exemplo")
Para adicionar um elemento a uma lista, podemos utilizar o método `append()`.
### Exemplo
```
lista_de_nomes = ['Ewerton', 'Gabriel', 'Lucas', 'Angelo']
lista_de_nomes.append('Gustavo')

print(lista_de_nomes)
```
## [Del](./exemplos/Listas/deletar.py "Verifique o script do exemplo")
Para remover um elemento de uma lista, usamos a palavra-chave `del` junto do índice do elemento que queremos remover:
```
lista_de_numeros = [10,25,390,35,40,50]

del lista_de_numeros[2]
print(lista_de_numeros)
```
Saída do terminal:
`[10, 25, 35, 40, 50]`
## [Insert( )](./exemplos/Listas/inserir.py "Verifique o script do exemplo")
insere um item na lista na posição indicada
### Exemplo
```
usuarios = ['Ewerton','João','Fernando']

usuarios.insert(1,'Felipe')
```
Saída do terminal: `['Ewerton', 'Felipe', 'João', 'Fernando']`