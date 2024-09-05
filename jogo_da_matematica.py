# JOÃO PEDRO MOREIRA DA FONSECA
# MARINA LIMA BOEIRA
# DOUGLAS RIBEIRO
# GUILHERME MONTOYA

# IMPORTS
import random
import os
import time

# função para limpar a tela e verificar o sistema operacional
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

# limpa a tela
limpar_tela()

# PONTUAÇÃO
pontos = 0

# Menu do jogo
print("Bem vindo ao Jogo de Matemática!")
print("Selecione uma das opções:")
print("1. JOGO INDIVIDUAL")
print("2. JOGO CONFRONTO")

# Escolha do jogador
escolha = input("Insíra a opção escolhida: ")

# limpa a tela
limpar_tela()

#--------------------------------------------- SINGLEPLAYER -------------------------
if escolha == "1":
    # Menu de difilculdade
    print("Selecione a dificuldade:")
    print("1. Fácil👶")
    print("2. Médio🤔")
    print("3. Difícil👿")

    # ESCOLHA DE DIFICULDADE DO JOGADOR
    dificuldade = input("Insíra a dificuldade escolhida: ")

    # limpa a tela
    limpar_tela()

    if dificuldade  == "1":
        dificuldade = "Fácil"
        numr1 = random.randint(-10, 10)
        numr2 = random.randint(-10, 10)
        numr3 = random.randint(-10, 10)
        numr4 = random.randint(-10, 10)
        numr5 = random.randint(-10, 10)
        numr6 = random.randint(-10, 10)
        numr7 = random.randint(-10, 10)
        numr8 = random.randint(-10, 10)
    elif dificuldade  == "2":
        dificuldade = "Média"
        numr1 = random.randint(-100, 100)
        numr2 = random.randint(-100, 100)
        numr3 = random.randint(-100, 100)
        numr4 = random.randint(-100, 100)
        numr5 = random.randint(-100, 100)
        numr6 = random.randint(-100, 100)
        numr7 = random.randint(-100, 100)
        numr8 = random.randint(-100, 100)
    elif dificuldade  == "3":
        dificuldade = "Difícil"
        numr1 = random.randint(-1000, 1000)
        numr2 = random.randint(-1000, 1000)
        numr3 = random.randint(-1000, 1000)
        numr4 = random.randint(-1000, 1000)
        numr5 = random.randint(-1000, 1000)
        numr6 = random.randint(-1000, 1000)
        numr7 = random.randint(-1000, 1000)
        numr8 = random.randint(-1000, 1000)
    else:
        print("Dificuldade inválida!")

    # limpa a tela
    limpar_tela()

    print(f"Você escolheu a dificuldade {dificuldade}.")
    print("Você tem 30 segundos para resolver cada uma das 4 equações")
    print("Começando em 3. . .")
    time.sleep(1)
    print("Começando em 2. . .")
    time.sleep(1)
    print("Começando em 1. . .")
    time.sleep(1)

    # limpa a tela
    limpar_tela()
    #--------------------------------------------- SOMA -------------------------
    # Inicializar o tempo
    tempo_ini1 = time.time()

    fconta1 = f"{numr1} + {numr2}"
    print(f"Resolva a seguinte equação: {fconta1}")
    fresposta1 = int(input("Sua resposta: "))

    if numr1 + numr2 == fresposta1:
        fpontos1 = 10
        print('Você acertou!')
    else:
        fpontos1 = 0
        print('Mais sorte na próxima vez!')

    # CALCULAR O TEMPO PASSADO E DIMINUIR A PONTUAÇÃO
    tempo_pas1 = time.time() - tempo_ini1
    if tempo_pas1 >= 5:
        tempo_excedido1 = tempo_pas1 - 5
        percentual_reducao = tempo_excedido1 * 0.02
        fpontos1 -= int(percentual_reducao * 10)

    # TERMINAR O JOGO DEPOIS DE 30S
    if tempo_pas1 >= 30:
        fpontos1 = 0
        print("Tempo esgotado!")

    time.sleep(1.1)

    # limpa a tela
    limpar_tela()

    #--------------------------------------------- SUBTRAÇÃO -------------------------
    # Inicializar o tempo
    tempo_ini2 = time.time()

    fconta2 = f"{numr3} - {numr4}"
    print(f"Resolva a seguinte equação: {fconta2}")
    fresposta2 = int(input("Sua resposta: "))

    if numr3 - numr4 == fresposta2:
        fpontos2 = 10
        print('Você acertou!')
    else:
        fpontos2 = 0
        print('Mais sorte na próxima vez!')

    # CALCULAR O TEMPO PASSADO E DIMINUIR A PONTUAÇÃO
    tempo_pas2 = time.time() - tempo_ini2
    if tempo_pas2 >= 5:
        tempo_excedido2 = tempo_pas2 - 5
        percentual_reducao = tempo_excedido2 * 0.02
        fpontos2 -= int(percentual_reducao * 10)

    # TERMINAR O JOGO DEPOIS DE 30S
    if tempo_pas2 >= 30:
        fpontos2 = 0
        print("Tempo esgotado!")

    time.sleep(1.1)

    # limpa a tela
    limpar_tela()

    #--------------------------------------------- MULTIPLICAÇÃO -------------------------
    # Inicializar o tempo
    tempo_ini3 = time.time()

    fconta3 = f"{numr5} * {numr6}"
    print(f"Resolva a seguinte equação: {fconta3}")
    fresposta3 = int(input("Sua resposta: "))

    if numr5 * numr6 == fresposta3:
        fpontos3 = 10
        print('Você acertou!')
    else:
        fpontos3 = 0
        print('Mais sorte na próxima vez!')

    # CALCULAR O TEMPO PASSADO E DIMINUIR A PONTUAÇÃO
    tempo_pas3 = time.time() - tempo_ini3
    if tempo_pas3 >= 5:
        tempo_excedido3 = tempo_pas3 - 5
        percentual_reducao = tempo_excedido3 * 0.02
        fpontos3 -= fpontos3 - int(percentual_reducao * 10)

    # TERMINAR O JOGO DEPOIS DE 30S
    if tempo_pas3 >= 30:
        fpontos3 = 0
        print("Tempo esgotado!")

    time.sleep(1.1)

    # limpa a tela
    limpar_tela()

    #--------------------------------------------- DIVISÃO -------------------------
    # Inicializar o tempo
    tempo_ini4 = time.time()

    fconta4 = f"{numr7} // {numr8}"
    print(f"Resolva a seguinte equação: {fconta4}")
    fresposta4 = int(input("Sua resposta: "))

    if numr7 // numr8 == fresposta4:
        fpontos4 = 10
        print('Você acertou!')
    else:
        fpontos4 = 0
        print('Mais sorte na próxima vez!')

    # CALCULAR O TEMPO PASSADO E DIMINUIR A PONTUAÇÃO
    tempo_pas4 = time.time() - tempo_ini4
    if tempo_pas4 >= 5:
        tempo_excedido4 = tempo_pas4 - 5
        percentual_reducao = tempo_excedido4 * 0.02
        fpontos4 -= int(percentual_reducao * 10)

    # TERMINAR O JOGO DEPOIS DE 30S
    if tempo_pas4 >= 30:
        fpontos4 = 0
        print("Tempo esgotado!")

    time.sleep(1.1)

    # limpa a tela
    limpar_tela()

    #-----CALCULO DE PONTOS
    pontos = fpontos1 + fpontos2 + fpontos3 + fpontos4

    #--------------------------------------------- CONCLUSÃO -------------------------
    total_tempo = int(tempo_pas1 + tempo_pas2 + tempo_pas3 + tempo_pas4)

    if  pontos == 40:
        print(f"Parabéns você conseguiu a pontuação máxima!")
        time.sleep(1)
        print("🎊🎉🥳")
        time.sleep(1)
        print("🎊🎉🥳")
        time.sleep(1)
        print("🎊🎉🥳")
        time.sleep(1)
        print("🎊🎉🥳")
    elif pontos < 40 and pontos > 21:
        print(f"Você foi muito bem com um total de {pontos} pontos!")
    elif pontos < 21 and pontos > 11:
        print(f"Você teve um total de {pontos} pontos, mais sorte na próxima!")
    else:
        print(f"Você foi muito mal e teve um total de {pontos} pontos!")

    print (f"Você terminou em {total_tempo} segundos.")

    #--------------------------------------------- MULTIPLAYER -------------------------
elif escolha == "2":
# Menu de difilculdade
    print("Selecione a dificuldade:")
    print("1. Fácil👶")
    print("2. Médio🤔")
    print("3. Díficil👿")

# ESCOLHA DE DIFICULDADE DO JOGADOR
    dificuldade = input("Insíra a dificuldade escolhida: ")
    if dificuldade  == "1":
        dificuldade = "Fácil"
        numr1 = random.randint(-10, 10)
        numr2 = random.randint(-10, 10)
        numr3 = random.randint(-10, 10)
        numr4 = random.randint(-10, 10)
        numr5 = random.randint(-10, 10)
        numr6 = random.randint(-10, 10)
        numr7 = random.randint(-10, 10)
        numr8 = random.randint(-10, 10)
        Mnumr1 = random.randint(-10, 10)
        Mnumr2 = random.randint(-10, 10)
        Mnumr3 = random.randint(-10, 10)
        Mnumr4 = random.randint(-10, 10)
        Mnumr5 = random.randint(-10, 10)
        Mnumr6 = random.randint(-10, 10)
        Mnumr7 = random.randint(-10, 10)
        Mnumr8 = random.randint(-10, 10)
    elif dificuldade  == "2":
        dificuldade = "Médio"
        numr1 = random.randint(-100, 100)
        numr2 = random.randint(-100, 100)
        numr3 = random.randint(-100, 100)
        numr4 = random.randint(-100, 100)
        numr5 = random.randint(-100, 100)
        numr6 = random.randint(-100, 100)
        numr7 = random.randint(-100, 100)
        numr8 = random.randint(-100, 100)
        Mnumr1 = random.randint(-100, 100)
        Mnumr2 = random.randint(-100, 100)
        Mnumr3 = random.randint(-100, 100)
        Mnumr4 = random.randint(-100, 100)
        Mnumr5 = random.randint(-100, 100)
        Mnumr6 = random.randint(-100, 100)
        Mnumr7 = random.randint(-100, 100)
        Mnumr8 = random.randint(-100, 100)
    elif dificuldade  == "3":
        dificuldade = "Difícil"
        numr1 = random.randint(-1000, 1000)
        numr2 = random.randint(-1000, 1000)
        numr3 = random.randint(-1000, 1000)
        numr4 = random.randint(-1000, 1000)
        numr5 = random.randint(-1000, 1000)
        numr6 = random.randint(-1000, 1000)
        numr7 = random.randint(-1000, 1000)
        numr8 = random.randint(-1000, 1000)
        Mnumr1 = random.randint(-1000, 1000)
        Mnumr2 = random.randint(-1000, 1000)
        Mnumr3 = random.randint(-1000, 1000)
        Mnumr4 = random.randint(-1000, 1000)
        Mnumr5 = random.randint(-1000, 1000)
        Mnumr6 = random.randint(-1000, 1000)
        Mnumr7 = random.randint(-1000, 1000)
        Mnumr8 = random.randint(-1000, 1000)
    else:
        print("Dificuldade inválida!")
    # limpa a tela
    limpar_tela()

    ply1 = input("Digite o nome do jogador N°1:")
    ply2 = input("Digite o nome do jogador N°2:")

    # limpa a tela
    limpar_tela()

    print(f"Você escolheu a dificuldade {dificuldade}.")
    print(f"{ply1} tem 30 segundos para resolver cada uma das 4 equações")
    print("Começando em 3. . .")
    time.sleep(1)
    print("Começando em 2. . .")
    time.sleep(1)
    print("Começando em 1. . .")
    time.sleep(1)

    # limpa a tela
    limpar_tela()
        #--------------------------------------------- SOMA PLAYER 1-------------------------
    # Inicializar o tempo
    tempo_ini1 = time.time()

    fconta1 = f"{numr1} + {numr2}"
    print(f"Resolva a seguinte equação: {fconta1}")
    fresposta1 = int(input("Sua resposta: "))

    if numr1 + numr2 == fresposta1:
        fpontos1 = 10
        print('Você acertou!')
    else:
        fpontos1 = 0
        print('Mais sorte na próxima vez!')

        # CALCULAR O TEMPO PASSADO E DIMINUIR A PONTUAÇÃO
        tempo_pas1 = time.time() - tempo_ini1
        if tempo_pas1 >= 5:
            tempo_excedido = tempo_pas1 - 5
            percentual_reducao = tempo_excedido * 0.02
            fpontos1 -= int(percentual_reducao * 10)

        # TERMINAR O JOGO DEPOIS DE 30S
        if tempo_pas1 >= 30:
            fpontos1 = 0
            print("Tempo esgotado!")

        time.sleep(1.1)

        # limpa a tela
        limpar_tela()

    #--------------------------------------------- SUBTRAÇÃO PLAYER 1 -------------------------
    # Inicializar o tempo
    tempo_ini2 = time.time()

    fconta2 = f"{numr3} - {numr4}"
    print(f"Resolva a seguinte equação: {fconta2}")
    fresposta2 = int(input("Sua resposta: "))

    if numr3 - numr4 == fresposta2:
        fpontos2 = 10
        print('Você acertou!')
    else:
        fpontos2 = 0
        print('Mais sorte na próxima vez!')

    # CALCULAR O TEMPO PASSADO E DIMINUIR A PONTUAÇÃO
    tempo_pas2 = time.time() - tempo_ini2
    if tempo_pas2 >= 5:
        tempo_excedido = tempo_pas2 - 5
        percentual_reducao = tempo_excedido * 0.02
        fpontos2 -= int(percentual_reducao * 10)

    # TERMINAR O JOGO DEPOIS DE 30S
    if tempo_pas2 >= 30:
        fpontos2 = 0
        print("Tempo esgotado!")

    time.sleep(1.1)

    # limpa a tela
    limpar_tela()

    #--------------------------------------------- MULTIPLICAÇÃO PLAYER 1 -------------------------
    # Inicializar o tempo
    tempo_ini3 = time.time()

    fconta3 = f"{numr5} * {numr6}"
    print(f"Resolva a seguinte equação: {fconta3}")
    fresposta3 = int(input("Sua resposta: "))

    if numr5 * numr6 == fresposta3:
        fpontos3 = 10
        print('Você acertou!')
    else:
        fpontos3 = 0
        print('Mais sorte na próxima vez!')

    # CALCULAR O TEMPO PASSADO E DIMINUIR A PONTUAÇÃO
    tempo_pas3 = time.time() - tempo_ini3
    if tempo_pas3 >= 5:
        tempo_excedido = tempo_pas3 - 5
        percentual_reducao = tempo_excedido * 0.02
        fpontos3 -= int(percentual_reducao * 10)

    # TERMINAR O JOGO DEPOIS DE 30S
    if tempo_pas3 >= 30:
        fpontos3 = 0
        print("Tempo esgotado!")

    time.sleep(1.1)

    # limpa a tela
    limpar_tela()

    #--------------------------------------------- DIVISÃO PLAYER 1 -------------------------
    # Inicializar o tempo
    tempo_ini4 = time.time()

    fconta4 = f"{numr7} // {numr8}"
    print(f"Resolva a seguinte equação: {fconta4}")
    fresposta4 = int(input("Sua resposta: "))

    if numr7 // numr8 == fresposta4:
        fpontos4 = 10
        print('Você acertou!')
    else:
        fpontos4 = 0
        print('Mais sorte na próxima vez!')

    # CALCULAR O TEMPO PASSADO E DIMINUIR A PONTUAÇÃO
        tempo_pas4 = time.time() - tempo_ini4
        if tempo_pas4 >= 5:
            tempo_excedido = tempo_pas4 - 5
            percentual_reducao = tempo_excedido * 0.02
            fpontos4 -= int(percentual_reducao * 10)

    # TERMINAR O JOGO DEPOIS DE 30S
    if tempo_pas4 >= 30:
        fpontos4 = 0
        print("Tempo esgotado!")

    time.sleep(1.1)

    # limpa a tela
    limpar_tela()

    #-----CALCULO DE PONTOS
    p1pontos = fpontos1 + fpontos2 + fpontos3 + fpontos4

    # limpa a tela
    limpar_tela()

    print(f"Agora é vez do segundo jogador.")
    print(f"{ply2} tem 30 segundos para resolver cada uma das 4 equações")
    print("Começando em 3. . .")
    time.sleep(1)
    print("Começando em 2. . .")
    time.sleep(1)
    print("Começando em 1. . .")
    time.sleep(1)

    # limpa a tela
    limpar_tela()

#--------------------------------------------- SOMA PLAYER 2 -------------------------
    # Inicializar o tempo
    tempo_ini1 = time.time()

    fconta1 = f"{Mnumr1} + {Mnumr2}"
    print(f"Resolva a seguinte equação: {fconta1}")
    fresposta1 = int(input("Sua resposta: "))

    if Mnumr1 + Mnumr2 == fresposta1:
        fmpontos1 = 10
        print('Você acertou!')
    else:
        fmpontos1 = 0
        print('Mais sorte na próxima vez!')

        # CALCULAR O TEMPO PASSADO E DIMINUIR A PONTUAÇÃO
        tempo_pas1M = time.time() - tempo_ini1
        if tempo_pas1M >= 5:
            tempo_excedido = tempo_pas1M - 5
            percentual_reducao = tempo_excedido * 0.02
            fmpontos1 -= int(percentual_reducao * 10)

        # TERMINAR O JOGO DEPOIS DE 30S
        if tempo_pas1M >= 30:
            fmpontos1 = 0
            print("Tempo esgotado!")

        time.sleep(1.1)

        # limpa a tela
        limpar_tela()

        #--------------------------------------------- SUBTRAÇÃO PLAYER 2 -------------------------
        # Inicializar o tempo
        tempo_ini2 = time.time()

        fconta2 = f"{Mnumr3} - {Mnumr4}"
        print(f"Resolva a seguinte equação: {fconta2}")
        fresposta2 = int(input("Sua resposta: "))

        if Mnumr3 - Mnumr4 == fresposta2:
            fmpontos2 = 10
            print('Você acertou!')
        else:
            fmpontos2 = 0
            print('Mais sorte na próxima vez!')

        # CALCULAR O TEMPO PASSADO E DIMINUIR A PONTUAÇÃO
        tempo_pas2M = time.time() - tempo_ini2
        if tempo_pas2M >= 5:
            tempo_excedido = tempo_pas2M - 5
            percentual_reducao = tempo_excedido * 0.02
            fmpontos2 -= int(percentual_reducao * 10)

        # TERMINAR O JOGO DEPOIS DE 30S
        if tempo_pas2M >= 30:
            fmpontos2 = 0
            print("Tempo esgotado!")

        time.sleep(1.1)

        # limpa a tela
        limpar_tela()

        #--------------------------------------------- MULTIPLICAÇÃO PLAYER 2 -------------------------
        # Inicializar o tempo
        tempo_ini3 = time.time()

        fconta3 = f"{Mnumr5} * {Mnumr6}"
        print(f"Resolva a seguinte equação: {fconta3}")
        fresposta3 = int(input("Sua resposta: "))

        if Mnumr5 * Mnumr6 == fresposta3:
            fmpontos3 = 10
            print('Você acertou!')
        else:
            fmpontos3 = 0
            print('Mais sorte na próxima vez!')

        # CALCULAR O TEMPO PASSADO E DIMINUIR A PONTUAÇÃO
        tempo_pas3M = time.time() - tempo_ini3
        if tempo_pas3M >= 5:
            tempo_excedido = tempo_pas3M - 5
            percentual_reducao = tempo_excedido * 0.02
            fmpontos3 -= int(percentual_reducao * 10)

        # TERMINAR O JOGO DEPOIS DE 30S
        if tempo_pas3M >= 30:
            fmpontos3 = 0
            print("Tempo esgotado!")

        time.sleep(1.1)

        # limpa a tela
        limpar_tela()

        #--------------------------------------------- DIVISÃO PLAYER 2 -------------------------
        # Inicializar o tempo
        tempo_ini4 = time.time()

        fconta4 = f"{Mnumr7} // {Mnumr8}"
        print(f"Resolva a seguinte equação: {fconta4}")
        fresposta4 = int(input("Sua resposta: "))

        if Mnumr7 // Mnumr8 == fresposta4:
            fmpontos4 = 10
            print('Você acertou!')
        else:
            fmpontos4 = 0
            print('Mais sorte na próxima vez!')

        # CALCULAR O TEMPO PASSADO E DIMINUIR A PONTUAÇÃO
            tempo_pas4M = time.time() - tempo_ini4
            if tempo_pas4M >= 5:
                tempo_excedido = tempo_pas4M - 5
                percentual_reducao = tempo_excedido * 0.02
                fmpontos4 -= int(percentual_reducao * 10)

        # TERMINAR O JOGO DEPOIS DE 30S
        if tempo_pas4M >= 30:
            fmpontos4 = 0
            print("Tempo esgotado!")

        time.sleep(1.1)

        # limpa a tela
        limpar_tela()

        #-----CALCULO DE PONTOS JOGADOR N°2
        p2pontos = fmpontos1 + fmpontos2 + fmpontos3 + fmpontos4
        
        #-----TEMPO TOTAL DE AMBOS OS JOGADORES
        tempo_total_ply1 = tempo_pas1 + tempo_pas2 + tempo_pas3 + tempo_pas4
        tempo_total_ply2 = tempo_pas1M + tempo_pas2M + tempo_pas3M + tempo_pas4M
        tempo_total = int(tempo_total_ply1 + tempo_total_ply2)
        
    if p1pontos <  p2pontos:
        print(f"Parabéns ao {ply2} você ganhou com {p2pontos} pontos no total!")
        print(f"Seu adversário teve apenas {p1pontos}.")
    elif p1pontos >  p2pontos:
        print(f"Parabéns ao {ply1} você ganhou com {p1pontos} pontos no total!!")
        print(f"Seu adversário teve apenas {p2pontos}.")
    else:
        print(f"Parabéns ao {ply1} e ao {ply2} você empataram com {p1pontos} pontos no total!")

    print(f"vocês passaram {tempo_total} segundos jogando juntos.")
    
else:
    print("Modo Inválido!")