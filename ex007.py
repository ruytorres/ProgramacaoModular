def soma(num1, num2):
    return num1 + num2
def subtracao(num1, num2):
    return num1 - num2
def divisao(num1, num2):
    return num1 / num2
def multiplicacao(num1, num2):
    return num1 * num2

escolha = int(input(
'''soma(1)
subtração(2)
divisão(3)
multiplicacao(4)
Digite qual operação você deseja realizar:
'''))
num1 = int(input('Digite um numero: '))
num2 = int(input('Digite outro numero: '))

if escolha == 1:
    resultado = soma(num1, num2)
elif escolha == 2:
    resultado = subtracao(num1, num2)
elif escolha == 3:
    resultado = divisao(num1, num2)
elif escolha == 4:
    resultado = multiplicacao(num1, num2)

print(f'O resultado é {resultado}')

