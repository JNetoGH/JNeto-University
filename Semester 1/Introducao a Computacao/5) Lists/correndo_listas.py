# GERCACAO AUTOMATICA DE QUADRADOS
SIZE: int = 10
squares: list = [0] * SIZE
for i in range(0, len(squares)):
    squares[i] = i * i
    print(f"[{i}]: {squares[i]}")

print("\n")
# CORRENDO LISTA SIMPLES (for):
squares2: list = [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]
for j in range(0, len(squares)):
    print(f"[{j}]: {squares[j]}")

print("\n")
# CORRENDO LISTA SIMPLES (while):
nomes: list = ["joao", "ana", "bianca"]
cont: int = 0
while cont < len(nomes):
    print(f"[{cont}] = {nomes[cont]}")
    cont = cont + 1

print("\n")
# CORRENDO LISTA SIMPLES (for each):
for elemento in nomes:
    print(f"{elemento}")

print("\n")
# CORRENDO LISTA DE SIMPLES (recursividade)
sobrenomes = ["mendes", "oliveira", "brito"]
def recursive(contador2:int = 0):
    print(f"[{contador2}] = {sobrenomes[contador2]}")
    contador2 = contador2 + 1
    if contador2 < len(sobrenomes):
        recursive(contador2)
recursive()
