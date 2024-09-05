# Imports
import os
import time

# Função para limpar a tela
def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

#--------------------------------------------- MENU

print("Bem vindo ao jogo da forca!")
stringA = input("Digite a palavra: ").lower()
numT = int(input("Digite o número máximo de tentativas: "))

# Limpa tela
limpar_tela()

#--------------------------------------------- PREPARAÇÃO

# REPRESENTA AS LETRAS NÃO IDENTIFICADAS
stringB = "-" * len(stringA)

# CONTADOR DE LETRAS ERRADAS
letras_erradas = ""

# CONTADOR DE TENTAVIAS
tent = 0

#--------------------------------------------- JOGO
# Enquanto  houver tentativas e ainda não foi acertado todas as letras
while tent < numT and stringA != stringB:

# Limpa tela
    limpar_tela()

    # Exibe as informações atuais do jogo
    print("Palavra atual:", stringB)
    print("Letras erradas:", letras_erradas)
    print("Tentativas restantes:", numT - tent)

    # Solicita um palpite
    palpite = input("Digite um caractere ou uma string:  ").lower()  # Converte para minúscula para facilitar a comparação

    # Verifica se o palpite é uma letra
    if palpite.isalpha():
        # Verifica se o palpite é um único caractere
        if len(palpite) == 1:
            # Verifica se a letra está na palavra
            achou_letra = False
            stringB2 = ""
            for i in range(len(stringA)):
                if stringA[i] == palpite:
                    stringB2 += palpite
                    achou_letra = True
                else:
                    stringB2 += stringB[i]

            stringB = stringB2

#--------------------------------------------- VERIFICAÇÃO DO PALPITE
            if not achou_letra:
                letras_erradas += palpite
                print("Letra não encontrada na palavra.")
                time.sleep(1.2)
        elif palpite == stringA:
            stringB = stringA
        else:
            print("Palavra incorreta.")
            time.sleep(1.2)
    else:
        print("Por favor, insira uma letra válida ou a palavra completa.")
        time.sleep(1.2)

    # Incrementa o contador de tentativas
    tent += 1

    # Limpa tela
    limpar_tela()

#--------------------------------------------- RESULTADO DO JOGO
if stringA == stringB:
    print("Parabéns, você ganhou em", tent, "tentativas")
else:
    print("Que pena. A palavra era", stringA)