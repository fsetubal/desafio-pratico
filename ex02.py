def converter_notas_em_graus(notas):
    graus = {
        'Dó': 'I',
        'Ré': 'II',
        'Mi': 'III',
        'Fá': 'IV',
        'Sol': 'V',
        'Lá': 'VI',
        'Si': 'VII'
    }
    graus_notas = []
    for nota in notas:
        if nota in graus:
            graus_notas.append(graus[nota])
    return graus_notas

# Exemplo de uso (Simulação sistema)
notas_musicais = ['Ré', 'Sol', 'Dó', 'Fá', 'Lá', 'Mi', 'Si']
graus_notas = converter_notas_em_graus(notas_musicais)
print(graus_notas)