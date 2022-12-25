def distancias(pos1, pos2):
    return max(abs(pos1[0] - pos2[0]), abs(pos1[1] - pos2[1]))

with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [x[:-1] for x in lines]

posiciones = set()
posiciones.add((0,0))
H_pos = [0,0]
T_pos = [0,0]

for x in lines:
    movimiento = x.split()
    if movimiento[0] == 'R':
        for i in range(int(movimiento[1])):
            H_pos[0] += 1
            if (distancias(H_pos, T_pos) > 1):
                T_pos = [H_pos[0] - 1, H_pos[1]]
                posiciones.add(tuple(T_pos))

    if movimiento[0] == 'L':
        for i in range(int(movimiento[1])):
            H_pos[0] += -1
            if (distancias(H_pos, T_pos) > 1):
                T_pos = [H_pos[0] + 1, H_pos[1]]
                posiciones.add(tuple(T_pos))

    if movimiento[0] == 'U':
        for i in range(int(movimiento[1])):
            H_pos[1] += 1
            if (distancias(H_pos, T_pos) > 1):
                T_pos = [H_pos[0], H_pos[1] - 1]
                posiciones.add(tuple(T_pos))

    if movimiento[0] == 'D':
        for i in range(int(movimiento[1])):
            H_pos[1] += -1
            if (distancias(H_pos, T_pos) > 1):
                T_pos = [H_pos[0], H_pos[1] + 1]
                posiciones.add(tuple(T_pos))

print(f'La cola ha visitado {len(posiciones)} posiciones.')
