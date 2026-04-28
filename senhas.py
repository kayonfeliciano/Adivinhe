import random
import string

letras = string.ascii_letters
numeros = string.digits
simbolos = string.punctuation


tamanho = input("Quantos caracters você quer na sua senha?")
tamanho = int(tamanho)
senha = ""

for caracter in range(tamanho - 2):
    letra_sorteada = random.choice(letras)
    senha = senha + letra_sorteada

numero = random.choice(numeros)
simbolos = random.choice(simbolos)
senha = senha + numero + simbolos
print(f"A sua senha gerada é: {senha}")
