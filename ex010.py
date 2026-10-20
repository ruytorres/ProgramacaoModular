def situacao_irrigacao(umidade_atual, umidade_minima):
    return umidade_atual < umidade_minima


def situacao_agua(agua_disponivel, agua_necessaria):
    return agua_disponivel >= agua_necessaria


def gerar_orientacao(necessita_irrigacao, agua_suficiente):
    if not necessita_irrigacao:
        return "Umidade adequada. Não é necessário irrigar."
    if agua_suficiente:
        return "Irrigação necessária e autorizada. Iniciando o processo..."
    else:
        return "Irrigação necessária, mas não há água suficiente no reservatório!"


def irrigacao_area(id_area, umidade_atual, umidade_minima, temperatura, agua_disponivel, agua_necessaria):
    irrigar = situacao_irrigacao(umidade_atual, umidade_minima)
    suficiente = situacao_agua(agua_disponivel, agua_necessaria) if irrigar else True
    orientacao = gerar_orientacao(irrigar, suficiente)

    print(f"Relatório da Área: {id_area} ")
    print(f"Temperatura Atual: {temperatura}")
    print(f"Umidade: {umidade_atual}% (Mínima recomendada: {umidade_minima}%)")
    print(f"Água Disponível: {agua_disponivel}L | Água Necessária: {agua_necessaria}L")
    print(orientacao)


area_id = input("Identificação da Área: ")
u_atual = float(input("Umidade atual do solo (%): "))
u_minima = float(input("Umidade mínima recomendada (%): "))
temp = float(input("Temperatura atual (°C): "))
vol_reservatorio = float(input("Quantidade de água disponível no reservatório (L): "))
vol_necessario = float(input("Quantidade de água necessária para irrigar (L): "))
irrigacao_area(area_id, u_atual, u_minima, temp, vol_reservatorio, vol_necessario)