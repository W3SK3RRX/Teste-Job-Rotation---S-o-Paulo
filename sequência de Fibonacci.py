num = int(input("Digite um número para verificar se ele pertence a sequência de fibonacci: "))
fib = [0, 1]
while fib[-1] < num:
    fib.append(fib[-1] + fib[-2])
if num in fib:
    print(f"O número {num} está presente na sequência!")
else:
    print(f"O número {num} não está presente na sequência")