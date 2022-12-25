with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [x for x in lines]
tam = len(lines[0])
montones = {i:[] for i in range(1,10)}

#Cargamos los datos de los montones iniciales
for i in range(8):
    j = 0
    while 4*j < tam:
        el = lines[i][4*j + 1:4*j + 2]
        if el != ' ':
            montones[j + 1].append(el)
        j += 1

#Invertimos las listas para que sean como pilas
for i in range(1,10):
    montones[i].reverse()

#Leemos las instrucciones
lines = lines[10:]

for l in lines:
    aux = []
    instruccion = l.split()
    cantidad = int(instruccion[1])
    origen = int(instruccion[3])
    destino = int(instruccion[5])
    for i in range(cantidad):
        elemento = montones[origen].pop()
        aux.append(elemento)

    aux.reverse()
    montones[destino] = montones[destino] + aux

lfinal = []
for i in range(1,10):
    lfinal.append(montones[i][-1])

print(''.join(lfinal))
