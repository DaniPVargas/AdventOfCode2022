def distancias(pos1, pos2):
    return max(abs(pos1[0] - pos2[0]), abs(pos1[1] - pos2[1]))

def diagonal(pos1, pos2):
    return abs(pos1[0] - pos2[0]) + abs(pos1[1] - pos2[1]) == 2

def arriba(pos1, pos2):
    return pos1[1] > pos2[1]

def lado(pos1, pos2):
    return pos1[0] > pos2[0]

def mover_cuerda(posiciones, cuerda, nudo, movimiento):
    if nudo < 9:
        esDiagonal = diagonal(cuerda[nudo], cuerda[nudo + 1])
        estaArriba = arriba(cuerda[nudo], cuerda[nudo + 1])
        estaDerecha = lado(cuerda[nudo], cuerda[nudo + 1])

    if movimiento == 'R':
        cuerda[nudo][0] += 1
        if(nudo == 9):
            posiciones.add(tuple(cuerda[nudo]))
            return
        if(distancias(cuerda[nudo], cuerda[nudo + 1]) > 1):
            if(esDiagonal):
                if(estaArriba):
                    mover_cuerda(posiciones, cuerda, nudo + 1, 'U')
                else:
                    mover_cuerda(posiciones, cuerda, nudo + 1, 'D')
                mover_cuerda(posiciones, cuerda, nudo + 1, 'R')
            else:
                mover_cuerda(posiciones, cuerda, nudo + 1, 'R')

    if movimiento == 'L':
        cuerda[nudo][0] += -1
        if(nudo == 9):
            posiciones.add(tuple(cuerda[nudo]))
            return
        if(distancias(cuerda[nudo], cuerda[nudo + 1]) > 1):
            if(esDiagonal):
                if(estaArriba):
                    mover_cuerda(posiciones, cuerda, nudo + 1, 'U')
                else:
                    mover_cuerda(posiciones, cuerda, nudo + 1, 'D')
                mover_cuerda(posiciones, cuerda, nudo + 1, 'L')
            else:
                mover_cuerda(posiciones, cuerda, nudo + 1, 'L')

    if movimiento == 'U':
        cuerda[nudo][1] += 1
        if(nudo == 9):
            posiciones.add(tuple(cuerda[nudo]))
            return
        if(distancias(cuerda[nudo], cuerda[nudo + 1]) > 1):
            if(esDiagonal):
                if(estaDerecha):
                    mover_cuerda(posiciones, cuerda, nudo + 1, 'R')
                else:
                    mover_cuerda(posiciones, cuerda, nudo + 1, 'L')
                mover_cuerda(posiciones, cuerda, nudo + 1, 'U')
            else:
                mover_cuerda(posiciones, cuerda, nudo + 1, 'U')

    if movimiento == 'D':
        cuerda[nudo][0] += -1
        if(nudo == 9):
            posiciones.add(tuple(cuerda[nudo]))
            return
        if(distancias(cuerda[nudo], cuerda[nudo + 1]) > 1):
            if(esDiagonal):
                if(estaDerecha):
                    mover_cuerda(posiciones, cuerda, nudo + 1, 'R')
                else:
                    mover_cuerda(posiciones, cuerda, nudo + 1, 'L')
                mover_cuerda(posiciones, cuerda, nudo + 1, 'D')
            else:
                mover_cuerda(posiciones, cuerda, nudo + 1, 'D')

def imprimir_cola(cuerda):
    pos = []
    for i in range(10):
        pos.append(cuerda[i])
    print(pos)

with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [x[:-1] for x in lines]
lines = ['R 5', 'U 8', 'L 8', 'D 3', 'R 17', 'D 10', 'L 25', 'U 20']

posiciones = set()
posiciones.add((0,0))

pos_cuerda =  {i:[0,0] for i in range(10)}

for m in lines:
    mov = m.split()
    for i in range(int(mov[1])):
        mover_cuerda(posiciones, pos_cuerda, 0, mov[0])
        imprimir_cola(pos_cuerda)


print(f'La cola ha visitado {len(posiciones)} posiciones.')
