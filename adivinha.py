import random
print("Bem vindo ao Jogo de Adivinhação!, as regras são simples, o computador irá escolher um número entre 1 e 100, e você terá que adivinhar qual é esse número. Você tem 10 tentativas para acertar o número, boa sorte!")
numero = random.randint(1,100)
tentativas = 10
while tentativas > 0:
    palpite = input("Dê o seu palpite:")
    if int(palpite) == numero:
        print ("Parabéns, você acertou o número!")
        break
    else:
        tentativas -= 1
        if tentativas > 0:
            print(f"Você errou! Tente novamente. Tentativas restantes: {tentativas}")
        else:
            print(f"Você perdeu! O número era {numero}.")