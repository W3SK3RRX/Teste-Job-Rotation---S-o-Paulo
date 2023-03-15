import json

with open('dados.json') as dados:
    faturamento = json.load(dados)

dias_com_faturamento = [dia for dia in faturamento if dia['valor'] > 0]

menor = min(dia['valor'] for dia in faturamento)
maior = max(dia['valor'] for dia in faturamento)

med = sum(dia['valor'] for dia in dias_com_faturamento) / len(dias_com_faturamento)

dias_acima_med = len([dia for dia in dias_com_faturamento if dia['valor'] > med])

print(f"Menor valor de faturamento: R$ {menor:.2f}")
print(f"Maior valor de faturamento: R$ {maior:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_med}")