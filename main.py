pedidos = [('F1', 'pouso'), ('F2', 'emergencia'), ('F3', 'decolagem'), ('F4', 'pouso'), ('F5', 'emergencia')]

fila = list(pedidos)

emergencias = [p for p in fila if p[1] == 'emergencia']
normais = [p for p in fila if p[1] != 'emergencia']

fila_ordenada = emergencias + normais

print(f"Fila inicial: {pedidos}")

limite = 3
atendidas = 0

for item in fila_ordenada:
    if atendidas < limite:
        print(f"Atendido: {item[0]}")
        atendidas += 1
    else:
        print(f"Recusado: {item[0]}")