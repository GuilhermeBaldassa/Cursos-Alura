import random

def jogo_adivinhacao():
    print("*********************************")
    print("Bem vindo ao jogo da adivinhação!")
    print("*********************************")


    #ramdom é uma biblioteca para gerar número aleatório.
    #randrange(1,101) --> vai trazer números aleatórios entre 1 e 100

    numero_secreto = random.randrange(1,101)
    pontos = 1000

    nivel = int(input("Escolha o nível de dificuldade: 1 - Fácil  2 - Médio  3 - Difícil : "))

    if(nivel == 1):
        total_de_tentativa = 10
    elif(nivel == 2):
        total_de_tentativa = 5
    else:
        total_de_tentativa = 3

    print("Você tem {} tentantivas".format(total_de_tentativa))

    for rodada in range (1,total_de_tentativa + 1):
        print("Tentativa: {} de {}".format(rodada, total_de_tentativa))

        chute = int(input("Digite um número entre 1 e 100: "))
        print("Você digitou: ", chute)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100")
            continue

        acertou = chute == numero_secreto
        maior   = chute > numero_secreto
        menor   = chute < numero_secreto


        if (acertou):
            print("Você acertou! E fez {}!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou!O seu chute foi maior que o número secreto\n")
            elif(menor):
                print("Você errou!O seu chute foi menor que o número secreto\n")
            pontos_perdidos = abs(numero_secreto - chute)
            pontos = pontos - pontos_perdidos

    print("Fim do jogo!")

if(__name__ == "__main__"):
    jogo_adivinhacao()