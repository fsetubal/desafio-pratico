import random

def encontrar_repetidos(a, b):
    repetidos = []
    for num in a:
        if num in b and num not in repetidos:
            repetidos.append(num)
    return repetidos

# Gerando os vetores aleatórios (Simulação do sistema)
vetor_a = random.choices(range(1, 100), k=20)
vetor_b = random.choices(range(1, 100), k=20)

# Exibindo os vetores gerados
print("Vetor A:", vetor_a)
print("Vetor B:", vetor_b)

# Encontrando os valores repetidos
resultado = encontrar_repetidos(vetor_a, vetor_b)

# Exibindo os valores repetidos
if len(resultado) > 0:
    print(f"Valores repetidos encontrados: {resultado}")
else:
    print("Nenhum valor repetido encontrado.")