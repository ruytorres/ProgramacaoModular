def calcular_media(nota1, nota2):
    media = (nota1 + nota2) / 2
    return media
def verificar_aprovacao(media):
    if media >= 7:
        return 'Aprovado'
    elif media < 7:
        return 'Reprovado'
def calcular_media_geral(soma_medias, total_estudantes):
    media_geral = soma_medias / total_estudantes
    return media_geral

total_aprovados = 0
soma_medias = 0.0

for i in range(1, 6):
    print(f"Estudante {i}:")
    nota1 = float(input("Digite a primeira nota: "))
    nota2 = float(input("Digite a segunda nota: "))
    media_aluno = calcular_media(nota1, nota2)
    resultado = verificar_aprovacao(media_aluno)

    print(f"Média: {media_aluno} | Resultado: {resultado}")
    soma_medias += media_aluno
    if resultado == 'Aprovado':
        total_aprovados += 1

media_turma = calcular_media_geral(soma_medias, 5)
print(f"Alunos aprovados: {total_aprovados}")
print(f"Média geral da turma: {media_turma}")

#Responsabilidades:
#Receber valores
# Definir funções(calcular_media/verificar_aprovação)