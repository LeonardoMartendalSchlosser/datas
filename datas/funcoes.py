from datetime import datetime, timedelta

FORMATO_PADRAO = "%Y-%m-%d"

def _converter_data(data_str):
    return datetime.strptime(data_str, FORMATO_PADRAO)

def adicionar_dias(data_str, dias):
    data = _converter_data(data_str)
    nova_data = data + timedelta(days=dias)
    return nova_data.strftime(FORMATO_PADRAO)

def subtrair_dias(data_str, dias):
    data = _converter_data(data_str)
    nova_data = data - timedelta(days=dias)
    return nova_data.strftime(FORMATO_PADRAO)

def diferenca_dias(data1, data2):
    d1 = _converter_data(data1)
    d2 = _converter_data(data2)
    return abs((d1 - d2).days)

def eh_final_de_semana(data_str):
    data = _converter_data(data_str)
    return data.weekday() >= 5  # 5=sábado, 6=domingo

def eh_dia_util(data_str):
    return not eh_final_de_semana(data_str)

def formatar_data(data_str, formato):
    data = _converter_data(data_str)
    return data.strftime(formato)

def data_hoje():
    return datetime.today().strftime(FORMATO_PADRAO)

def data_valida(data_str):
    try:
        _converter_data(data_str)
        return True
    except ValueError:
        return False
