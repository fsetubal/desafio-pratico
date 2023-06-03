from datetime import datetime

def calcular_tempo_casa(data_admissao):
    data_formatada = datetime.strptime(data_admissao, "%d/%m/%Y")
    data_atual = datetime.now()
    tempo_casa = data_atual - data_formatada

    return tempo_casa.days

def calcular_emprestimo():
    nome = input("Nome do colaborador: ")
    data_admissao = input("Data de admissão (dd/mm/aaaa): ")
    salario_atual = float(input("Salário atual(digite somente números): "))
    valor_emprestimo_original = int(input("Valor de empréstimo desejado(digite somente números): "))
    valor_emprestimo = valor_emprestimo_original

    if calcular_tempo_casa(data_admissao) <= 1825:
        print("Agradecemos seu interesse, mas você não atende os requisitos mínimos do programa.")
        return

    if valor_emprestimo % 2 != 0:
        print("Insira um valor válido!")
        return

    if valor_emprestimo > salario_atual * 2:
        print("Agradecemos seu interesse, mas você não atende os requisitos mínimos do programa.")
        return

    opcao = int(input("De qual forma deseja retirar o valor em dinheiro vivo?\n1. Notas de maior valor\n2. Notas de menor valor\n3. Notas meio a meio\nEscolha a opção desejada(digite 1, 2 ou 3): "))

    if opcao == 1:
        # Cálculo das notas de maior valor
        notas_maior_valor = {
            100: valor_emprestimo // 100,
            50: (valor_emprestimo % 100) // 50
        }

        print(f"Valor empréstimo: {valor_emprestimo_original} reais")
        print("Notas de maior valor:")
        for nota, quantidade in notas_maior_valor.items():
            if quantidade > 0:
                print(f"   {quantidade} x {nota} reais")

    elif opcao == 2:
        # Cálculo das notas de menor valor
        notas_menor_valor = {
            20: valor_emprestimo // 20,
            10: (valor_emprestimo % 20) // 10,
            5: (valor_emprestimo % 10) // 5,
            2: (valor_emprestimo % 5) // 2
        }

        print(f"Valor empréstimo: {valor_emprestimo_original} reais")
        print("Notas de menor valor:")
        for nota, quantidade in notas_menor_valor.items():
            if quantidade > 0:
                print(f"   {quantidade} x {nota} reais")

    elif opcao == 3:
        # Cálculo das notas meio a meio
        valor_meio_a_meio = valor_emprestimo // 2
        notas_meio_a_meio_maior = {
            100: valor_meio_a_meio // 100,
            50: (valor_meio_a_meio % 100) // 50,
            20: (valor_meio_a_meio % 50) // 20,
            5: (valor_meio_a_meio % 20) // 5
        }
        notas_meio_a_meio_menor = {
            20: valor_meio_a_meio // 20,
            10: (valor_meio_a_meio % 20) // 10,
            5: (valor_meio_a_meio % 10) // 5,
            2: (valor_meio_a_meio % 5) // 2
        }

        print(f"Valor empréstimo: {valor_emprestimo_original} reais")
        print("Notas meio a meio:")
        print(f"   {valor_meio_a_meio} reais em notas de maior valor:")
        for nota, quantidade in notas_meio_a_meio_maior.items():
            if quantidade > 0:
                print(f"      {quantidade} x {nota} reais")

        print(f"   {valor_meio_a_meio} reais em notas de menor valor:")
        for nota, quantidade in notas_meio_a_meio_menor.items():
            if quantidade > 0:
                print(f"      {quantidade} x {nota} reais")

calcular_emprestimo()