import requests

cidade = input("Essa é uma ferramenta criada para te ajudar a verificar a previsão do tempo de sua localidade, qual o nome da sua cidade?")

chave = "95607ca49aaa48d26c13905da4add672"
baseURL = f"https://api.openweathermap.org/data/2.5/weather?q={cidade}&appid={chave}&units=metric&lang=pt_br"

retorno = requests.get(baseURL)
retorno = retorno.json()

if retorno.get("cod") == 200:
    clima_atual = retorno["weather"][0]["description"]
    temperatura_atual = retorno["main"]["temp"]
    print(f"A temperatura atual em {cidade.title()} é {temperatura_atual:.0f}°C {clima_atual}")
else:
    print("Desculpe não conseguimos encontrar a cidade, verifique se o nome está correto.")