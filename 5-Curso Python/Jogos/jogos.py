import forca
import adivinhacao

def escolhe_jogo():
    print("*****************")
    print("Escolha seu jogo!")
    print("*****************")

    print("Escolha um jogo: 1 - Forca / 2 - Adivinhação")
    jogo = int(input("Qual jogo?"))

    if(jogo == 1):
        print("Jogando forca")
        forca.jogo_forca()
    elif(jogo == 2):
        print("Jogando Adivinhação")
        adivinhacao.jogo_adivinhacao()

if(__name__ == "__main__"):
    escolhe_jogo()