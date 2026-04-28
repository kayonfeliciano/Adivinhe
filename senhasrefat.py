import random
import string

caracteres = string.ascii_letters + string.digits + string.punctuation

tamanho = input("Quantos caracters você quer na sua senha?")
if tamanho.isdigit():
    tamanho = int(tamanho)

    if tamanho < 4 :
        print("A senha precisa conter no mimino 4 caracteres.")
    else :
        lista_senha = random.choices(caracteres, k=tamanho)
        senha = "".join(lista_senha)
        print(f"A senha senha é: {senha}")
else : 
    print(f"Erro: Por favor, digite um número inteiro")