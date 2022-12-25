with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [x for x in lines]

figuras = {'A': 0, 'B': 1, 'C': 2}
figuras2 = {'X': 0, 'Y': 1, 'Z': 2}
puntos = {'X': 0, 'Y': 3, 'Z': 6}

matriz_accion = [['C', 'A', 'B'], ['A', 'B', 'C'], ['B', 'C', 'A']]

puntuacion = 0

for l in lines:
    accion = l.split()
    puntuacion += puntos[accion[1]]
    gesto = matriz_accion[figuras[accion[0]]][figuras2[accion[1]]]
    puntuacion += figuras[gesto] + 1

print(puntuacion)
