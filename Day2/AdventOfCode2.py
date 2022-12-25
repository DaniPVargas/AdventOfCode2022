with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [x for x in lines]

figuras = {'X': 0, 'Y': 1, 'Z': 2}
figuras2 = {'A': 0, 'B': 1, 'C': 2}

matriz_puntos = [[3, 6, 0], [0, 3, 6], [6, 0, 3]]

puntuacion = 0

for l in lines:
    accion = l.split()
    puntuacion += figuras[accion[1]] + 1
    puntuacion += matriz_puntos[figuras2[accion[0]]][figuras[accion[1]]]

print(puntuacion)
