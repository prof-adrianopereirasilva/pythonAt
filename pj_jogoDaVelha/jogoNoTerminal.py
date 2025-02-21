# Função para exibir o tabuleiro
def imprimir_tabuleiro(tabuleiro):
    print(f"\n {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]} ")
    print("---|---|---|---")
    print(f" {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]} ")
    print("---|---|---|---")
    print(f" {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]} \n")

# Função para verificar se há um vencedor
def verificar_vencedor(tabuleiro, jogador):
    combinacoes_vencedoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
        [0, 4, 8], [2, 4, 6]  # Diagonais
    ]
    for combinacao in combinacoes_vencedoras:
        if tabuleiro[combinacao[0]] == tabuleiro[combinacao[1]] == tabuleiro[combinacao[2]] == jogador:
            return True
    return False

# Função para verificar se o jogo terminou (empate ou vencedor)
def jogo_terminado(tabuleiro):
    # Verificar se há vencedor
    for jogador in ['X', 'O']:
        if verificar_vencedor(tabuleiro, jogador):
            return True, jogador

    # Verificar se o tabuleiro está cheio (empate)
    if all(campo != ' ' for campo in tabuleiro):
        return True, 'Empate'
    
    return False, None

# Função principal para rodar o jogo
def jogar():
    tabuleiro = [' ' for _ in range(9)]  # Tabuleiro vazio
    jogador_atual = 'X'  # Jogador inicial
    em_andamento = True  # O jogo está em andamento

    while em_andamento:
        imprimir_tabuleiro(tabuleiro)

        # Solicitar a jogada do jogador atual
        jogada = int(input(f"Jogador {jogador_atual}, escolha uma posição (1-9): ")) - 1

        if tabuleiro[jogada] == ' ':
            tabuleiro[jogada] = jogador_atual
        else:
            print("Posição já ocupada! Tente outra.")
            continue

        # Verificar se o jogo terminou
        terminou, vencedor = jogo_terminado(tabuleiro)
        if terminou:
            imprimir_tabuleiro(tabuleiro)
            if vencedor == 'Empate':
                print("O jogo terminou em empate!")
            else:
                print(f"Jogador {vencedor} venceu!")
            em_andamento = False
        else:
            # Alternar o jogador
            jogador_atual = 'O' if jogador_atual == 'X' else 'X'

# Rodar o jogo
jogar()
