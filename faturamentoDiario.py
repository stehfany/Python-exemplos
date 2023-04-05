import json


with open("dados.json", "r") as file:
    faturamento_mensal = json.load(file)

dias_faturamento = [faturamento for faturamento in faturamento_mensal.values() if faturamento != 0]
media_mensal = sum(dias_faturamento) / len(dias_faturamento)

menor_faturamento = min(faturamento_mensal.values())
maior_faturamento = max(faturamento_mensal.values())

dias_acima_da_media = sum(1 for faturamento in dias_faturamento if faturamento > media_mensal)

print(f"Menor valor de faturamento: R$ {menor_faturamento:.2f}")
print(f"Maior valor de faturamento: R$ {maior_faturamento:.2f}")
print(f"Dias com faturamento acima da média mensal: {dias_acima_da_media}")