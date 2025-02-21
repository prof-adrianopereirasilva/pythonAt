from flask import Flask, render_template, request, redirect, url_for, make_response

app = Flask(__name__)

# Função para verificar o vencedor
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
    for jogador in ['X', 'O']:
        if verificar_vencedor(tabuleiro, jogador):
            return True, jogador
    if all(campo != ' ' for campo in tabuleiro):
        return True, 'Empate'
    return False, None

@app.route("/", methods=["GET", "POST"])
def index():
    # Inicializando o tabuleiro e o jogador atual
    if 'tabuleiro' not in request.cookies or 'jogador_atual' not in request.cookies:
        tabuleiro = [' ' for _ in range(9)]  # Tabuleiro vazio
        jogador_atual = 'X'  # Jogador inicial
    else:
        tabuleiro = request.cookies.get('tabuleiro').split(',')
        jogador_atual = request.cookies.get('jogador_atual')

    if request.method == "POST":
        if 'reiniciar' in request.form:  # Se o botão de reiniciar for pressionado
            # Limpar os cookies e reiniciar o jogo
            resp = make_response(redirect(url_for('index')))
            resp.set_cookie('tabuleiro', ','.join([' ' for _ in range(9)]))  # Reiniciar o tabuleiro
            resp.set_cookie('jogador_atual', 'X')  # Reiniciar o jogador atual
            return resp

        jogada = int(request.form['jogada'])
        if tabuleiro[jogada] == ' ':
            tabuleiro[jogada] = jogador_atual
            terminou, vencedor = jogo_terminado(tabuleiro)

            if terminou:
                resp = make_response(render_template('index.html', tabuleiro=tabuleiro, vencedor=vencedor))
                resp.set_cookie('tabuleiro', ','.join(tabuleiro))
                resp.set_cookie('jogador_atual', jogador_atual)
                return resp

            # Alternar o jogador
            jogador_atual = 'O' if jogador_atual == 'X' else 'X'

        # Atualizando os cookies com o novo estado
        resp = make_response(redirect(url_for('index')))
        resp.set_cookie('tabuleiro', ','.join(tabuleiro))
        resp.set_cookie('jogador_atual', jogador_atual)
        return resp

    return render_template('index.html', tabuleiro=tabuleiro, vencedor=None)

if __name__ == "__main__":
    app.run(debug=True)
