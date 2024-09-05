import turtle
import random
import time

# Variáveis globais para controle de estado
mat = []
mat_exib = []
exibir_contador = 0
jogo_em_andamento = False
pontos = 0
erros = 0
tamanho = 0
primeira_escolha = None
usos_exibir_restantes = 2  # Inicializa com 2 usos restantes

# Lista de emojis para o jogo da memória
emojis = ["😀", "😁", "😂", "🤣", "😃", "😄", "😅", "😆", "😉", "😊", "😋", "😎", "😍", "😘", "🥰", "😗", "😙", "😚", "🙂", "🤗", "🤩", "🤔", "🤨", "😐", "😑", "😶", "🙄", "😏", "😣", "😥", "😮", "🤐"]

# Função para criar a matriz de acordo com a dificuldade
def criar_matriz(dificuldade):
    global tamanho
    # Define o tamanho da matriz
    if dificuldade == "facil":
        tamanho = 4
    elif dificuldade == "medio":
        tamanho = 6
    elif dificuldade == "dificil":
        tamanho = 8
    else:
        raise ValueError("Dificuldade inválida. Escolha entre facil, medio ou dificil.")

    # Gera uma lista de pares de emojis aleatórios
    random.shuffle(emojis)
    selecionados = emojis[:(tamanho * tamanho) // 2] * 2
    random.shuffle(selecionados)

    # Cria a matriz de respostas e a matriz de exibição
    mat = []
    mat_exib = []
    for i in range(tamanho):
        mat.append(selecionados[i * tamanho:(i + 1) * tamanho])
        mat_exib.append(["#" for _ in range(tamanho)])
    
    return mat, mat_exib

# Função para atualizar a matriz com base nas jogadas do jogador
def atualiza(pos1, pos2, mat, mat_exib):
    global pontos, erros
    x1, y1 = pos1
    x2, y2 = pos2
    if mat[x1][y1] == mat[x2][y2]:
        mat_exib[x1][y1] = mat[x1][y1]
        mat_exib[x2][y2] = mat[x2][y2]
        pontos += 1
    else:
        mat_exib[x1][y1] = "#"
        mat_exib[x2][y2] = "#"
        erros += 1
    return mat, mat_exib

# Função para exibir a matriz de respostas por 3 segundos
def exibir_resp(mat):
    global exibir_contador, usos_exibir_restantes
    if exibir_contador < 2 and usos_exibir_restantes > 0:
        exibir_contador += 1
        usos_exibir_restantes -= 1  # Decrementa o contador de usos
        desenhar_matriz(mat)
        time.sleep(3)
        desenhar_matriz(mat_exib)
        turtle.update()  # Adiciona atualização após o tempo de espera

# Função para desenhar a matriz usando Turtle
def desenhar_matriz(mat_exib):
    turtle.clear()
    for i in range(tamanho):
        for j in range(tamanho):
            turtle.penup()
            turtle.goto(j * 40 - 160, -i * 40 + 160)
            turtle.pendown()
            turtle.write(mat_exib[i][j], align="center", font=("Arial", 16, "normal"))
            turtle.penup()
            turtle.goto(j * 40 - 180, -i * 40 + 180)
            turtle.pendown()
            for _ in range(4):
                turtle.forward(40)
                turtle.right(90)
    desenhar_botao(-200, -260, 120, 50, "Desistir", "lightcoral", "black")
    desenhar_botao(100, -260, 120, 50, "Exibir Respostas", "lightblue", "black")
    desenhar_pontuacao()
    desenhar_erros()
    turtle.hideturtle()
    turtle.update()  # Atualiza a tela para mostrar o desenho

    # Desenha o contador de usos do botão
    turtle.penup()
    turtle.goto(220, -300)
    turtle.pendown()
    turtle.write(f"Usos: {usos_exibir_restantes}", align="center", font=("Arial", 12, "normal"))
    

# Função para desenhar um botão
def desenhar_botao(x, y, largura, altura, texto, cor_fundo, cor_texto):
    turtle.penup()
    turtle.goto(x, y)
    turtle.pendown()
    turtle.fillcolor(cor_fundo)
    turtle.begin_fill()
    for _ in range(2):
        turtle.forward(largura)
        turtle.right(90)
        turtle.forward(altura)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    turtle.goto(x + largura / 2, y - altura / 2)
    turtle.pendown()
    turtle.color(cor_texto)
    turtle.write(texto, align="center", font=("Arial", 12, "normal"))
    turtle.color("black")

# Função para desenhar a pontuação
def desenhar_pontuacao():
    turtle.penup()
    turtle.goto(200, 150)
    turtle.pendown()
    turtle.write(f"Pontos: {pontos}", align="center", font=("Arial", 16, "bold"))

# Função para desenhar os erros
def desenhar_erros():
    turtle.penup()
    turtle.goto(200, 120)
    turtle.pendown()
    turtle.write(f"Erros: {erros}", align="center", font=("Arial", 16, "bold"))

# Função para desenhar a interface inicial
def desenhar_interface_inicial():
    turtle.clear()
    turtle.penup()
    turtle.goto(0, 200)
    turtle.pendown()
    turtle.write("Jogo da Memória", align="center", font=("Arial", 24, "bold"))
    desenhar_botao(-60, 50, 120, 40, "Fácil", "lightgreen", "black")
    desenhar_botao(-60, 0, 120, 40, "Médio", "yellow", "black")
    desenhar_botao(-60, -50, 120, 40, "Difícil", "red", "black")
    turtle.update()  # Adiciona atualização após o desenho

# Função para iniciar o jogo com a dificuldade selecionada
def iniciar_jogo(dificuldade):
    global mat, mat_exib, exibir_contador, jogo_em_andamento, pontos, erros, primeira_escolha, usos_exibir_restantes
    exibir_contador = 0
    pontos = 0
    erros = 0
    primeira_escolha = None
    usos_exibir_restantes = 2  # Reinicia o contador de usos

    mat, mat_exib = criar_matriz(dificuldade)
    desenhar_matriz(mat_exib)
    jogo_em_andamento = True

# Função para encerrar o jogo
def encerrar_jogo():
    global jogo_em_andamento
    jogo_em_andamento = False
    desenhar_interface_inicial()

# Função para verificar clique nos botões
def clique(x, y):
    global jogo_em_andamento, primeira_escolha, mat, mat_exib
    if not jogo_em_andamento:
        # Verifica se o clique está dentro do botão "Fácil"
        if -60 <= x <= 60 and 10 <= y <= 50:
            iniciar_jogo("facil")
        # Verifica se o clique está dentro do botão "Médio"
        elif -60 <= x <= 60 and -40 <= y <= 0:
            iniciar_jogo("medio")
        # Verifica se o clique está dentro do botão "Difícil"
        elif -60 <= x <= 60 and -90 <= y <= -50:
            iniciar_jogo("dificil")
    else:
        # Verifica se o clique está dentro do botão "Desistir"
        if -200 <= x <= -80 and -300 <= y <= -260:
            encerrar_jogo()
        # Verifica se o clique está dentro do botão "Exibir Respostas"
        elif 100 <= x <= 220 and -300 <= y <= -260:
            exibir_resp(mat)
        else:
            # Verifica se o clique está dentro da área da matriz
            if -180 <= x <= 180 and -180 <= y <= 180:
                coluna = int((x + 180) // 40)
                linha = int((180 - y) // 40)
                if mat_exib[linha][coluna] == "#":
                    if primeira_escolha is None:
                        primeira_escolha = (linha, coluna)
                        mat_exib[linha][coluna] = mat[linha][coluna]
                        desenhar_matriz(mat_exib)
                        turtle.update()  # Adiciona atualização após mostrar o primeiro emoji
                    else:
                        segunda_escolha = (linha, coluna)
                        mat_exib[linha][coluna] = mat[linha][coluna]
                        desenhar_matriz(mat_exib)
                        turtle.update()  # Adiciona atualização após mostrar o segundo emoji
                        time.sleep(1)
                        mat, mat_exib = atualiza(primeira_escolha, segunda_escolha, mat, mat_exib)
                        primeira_escolha = None
                        desenhar_matriz(mat_exib)
                        turtle.update()  # Adiciona atualização após atualizar a matriz
                        # Verifica se o jogo acabou
                        if all(emoji != "#" for linha in mat_exib for emoji in linha):
                            turtle.clear()
                            turtle.penup()
                            turtle.goto(0, 0)
                            turtle.pendown()
                            turtle.write(f"Parabéns! Você venceu!\nPontos: {pontos}\nErros: {erros}", align="center", font=("Arial", 24, "bold"))
                            turtle.update()
                            jogo_em_andamento = False
                            time.sleep(3)
                            encerrar_jogo()
    turtle.update()

# Configuração inicial do Turtle
turtle.speed(0)
turtle.hideturtle()
turtle.listen()
turtle.onscreenclick(clique)
turtle.tracer(0)  # Desliga as atualizações automáticas da tela

# Desenha a interface inicial
desenhar_interface_inicial()

turtle.update()  # Atualiza a tela de uma vez

turtle.done()