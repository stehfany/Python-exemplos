text = input("Digite um texto para inverter: ")

texto_invertido = ""

for i in range(len(text)-1, -1, -1):
    texto_invertido += text[i]

print(f"Texto invertido: {texto_invertido}")