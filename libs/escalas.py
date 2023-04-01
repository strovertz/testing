def escala_maturacao_soja(dias_desde_plantio):
    limites_dias = {
        'imatura': 60,
        'emergindo': 90,
        'madura': 120,
        'passada': 150
    }
    cores = {
        'imatura': 'green',
        'emergindo': 'yellow',
        'madura': 'orange',
        'passada': 'red'
    }

    for maturidade, limite in limites_dias.items():
        if dias_desde_plantio <= limite:
            return cores[maturidade]

    return cores['passada']

def situacao_maturidade(dias_desde_plantio):
    """
    Função que retorna a situação de maturidade com base nos dias desde o plantio.

    Args:
    - dias_desde_plantio: int, dias desde o plantio.

    Returns:
    - str, situação de maturidade.
    """
    if dias_desde_plantio <= 20:
        return "Em germinação"
    elif dias_desde_plantio <= 40:
        return "Em desenvolvimento vegetativo"
    elif dias_desde_plantio <= 80:
        return "Em floração"
    elif dias_desde_plantio <= 120:
        return "Em enchimento de grãos"
    else:
        return "Maduro"
