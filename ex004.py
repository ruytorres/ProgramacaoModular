
#Tarefa 2:
#Módulo: Média (recebe 3 notas e calcula a média final do aluno)
def Calcular_Media(nota1, nota2, nota3):
    media = (nota1 + nota2 + nota3) / 3
    return media

#Tarefa 3:
#Módulo: Situação do aluno (decidir se o aluno foi aprovado ou reprovado)
def Situacao_Aluno(media_final):
    if media_final >= 7:
        return "Aprovado"
    else:
        return "Reprovado"

#Tarefa 1:
#Módulo: Receber valores e valida-los(Módulo de entrada)
while True:
    nota1 = float(input("Digite a primeira nota: "))
    if 0 <= nota1 <= 10:
        break
while True:
    nota2 = float(input("Digite a segunda nota: "))
    if 0 <= nota1 <= 10:
        break
while True:
    nota3 = float(input("Digite a terceira nota: "))
    if 0 <= nota1 <= 10:
        break
media_final = Calcular_Media(nota1, nota2, nota3)
relatorio_aluno = Situacao_Aluno(media_final)
print('O aluno ficou com {:.2f} de média final e está {}'.format(media_final, relatorio_aluno))

'''
Programa principal
        ▼ (Envia as notas)
Função Calcular_Media
        ▼ (retorna apenas a média)
Programa principal
        ▼ (Envia a média)
Função verificar_situação
        ▼ (Envia "aprovado" ou "reprovado")
      print
'''