texto = "bom dia"
texto_invertido = ""

for i in range(len(texto)-1,-1,-1):
    texto_invertido += texto[i]

print(texto_invertido)