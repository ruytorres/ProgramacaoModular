def  Celsius_Fahreinheit(num):
    return num * 1.8 + 32

def Fahrenheit_Celsius(num):
    return (num-32) / 1.8

def Celsius_Kelvin(num):
    return num + 273.15
print('Convertendo temperaturas!')
print('1-Celsius para Fahrenheit')
print('2-Fahrenheit para Celsius')
print('3-Celsius para Kelvin')
num = int(input('Digite o número da conversão desejada:'))
if num == 1:
    temperatura = Celsius_Fahreinheit(num)
    print(temperatura)
elif num == 2:
    temperatura = Fahrenheit_Celsius(num)
    print(temperatura)
elif num == 3:
    temperatura = Celsius_Kelvin(num)
    print(temperatura)
else:
    print('Número inválido')

"""
Por que é preferível criar funções diferentes para as conversões em vez de colocar
todos os cálculos diretamente no programa principal?
Fica mais fácil identificar qual a conversão que o usuário pede por fora da função, depois é chamado apenas a função específica.
"""




