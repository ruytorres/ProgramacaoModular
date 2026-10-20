def quadrado(num):
    return num ** 2

num = int(input('Digite um número para descobrir o quadrado: '))
resultado = quadrado(num)
print('O quadrado de {} é {}'.format(num,resultado))