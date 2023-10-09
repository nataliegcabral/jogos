import random


def jogar():

    print("---------------------------------")
    print("Bem-vindo ao jogo da Adivinhação!")
    print("---------------------------------")

    numero_secreto = random.randrange(1, 101)
    tentativas = 0
    pontos = 1000

    print("--Níveis--")
    print("(1) Fácil \n(2) Médio \n(3) Difícil ")
    nivel = int(input("Escolha o nível de dificuldade: "))

    if nivel == 1:
        tentativas = 20
    elif nivel == 2:
        tentativas = 10
    elif nivel == 3:
        tentativas = 5
    else:
        print("Digite um nível válido!")

    for rodada in range(1, tentativas + 1):
        print("Tentativas {} de {}".format(rodada, tentativas))

        chute = int(input("Digite um número inteiro entre 1 e 100: "))

        if chute < 1 or chute > 100:
            print("Você deve digitar um número entre 1 e 100!\n")
            continue

        print("Você digitou", chute, "\n")

        acertou = numero_secreto == chute
        menor = chute > numero_secreto
        maior = chute < numero_secreto
        pontos_perdidos = abs(numero_secreto - chute)

        if acertou:
            print("Você acertou!\n".format(pontos))
            break
        elif menor:
            print('Errou! O número secreto é menor!\n')
            pontos = pontos - pontos_perdidos
        elif maior:
            print('Errou! O número secreto é maior!\n')
            pontos = pontos - pontos_perdidos
        else:
            print('Algo deu errado...\n')

    print("Fim de jogo! O número secreto era {}.\nPontuação: {}".format(numero_secreto, pontos))

if(__name__ == "__main__"):
    jogar()