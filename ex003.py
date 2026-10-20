def impar_par(num):
    if num % 2 == 0:
        return "Par"
    else:
        return "Impar"

num = int(input('Digite um número para verificar se ele é par ou impar: '))
resultado = impar_par(num)
print(resultado)

#Qual informação entra na função? Apenas o número digitado pelo usuário
#Qual informação sai da função? Uma string indicando se o número de input é par ou ímpar
#A leitura do número deveria ocorrer dentro da função ou no programa principal?
#A leitura deve ser feita fora da função para podermos reutilizar o código e organiza-lo apenas chamando funções destinadas ao que se pede.
