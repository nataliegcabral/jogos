import forca
import adivinhacao

print("---------------------------------")
print("Bem-vindo a sala de jogos Python!")
print("---------------------------------")

print("--Jogos--")
print("(1)Adivinhação\n(2)Forca")
jogo = int(input("Escolha o jogo que você quer jogar: "))

if jogo == 1:
    print("Jogando Adivinhação...")
    adivinhacao.jogar()
elif jogo == 2:
    print("Jogando Forca...")
    forca.jogar()
else:
    print("Escolha um jogo válido!")
