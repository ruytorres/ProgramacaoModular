#Módulo: Calcular IMC
def Calcular_IMC(peso, altura):
    IMC = (peso / (altura * altura))
    return IMC  #Valor de retorno
#Médulo: Situação da pessoa
def Situacao(IMC):
    if IMC < 18.5:
        return "Magra" 
    elif 18.5 <= IMC < 25:
        return "Peso normal"
    else:
        return 'Obesidade'

#Módulo: Rebecer dados
peso = float(input('Digite o seu peso em quilogramas: '))
altura = float(input('Digite sua altura em metros: '))
print(Situacao(Calcular_IMC(peso, altura)))
print(Calcular_IMC(peso, altura))
