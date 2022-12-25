#------------------------ DECLARACIÓN DE FUNCIONES -----------------------------
def visible_desde_arriba(posicion, mapa):
    es_visible = True
    count = 0
    for i in range(posicion[0] - 1, -1, -1):
        count += 1
        if mapa[i][posicion[1]] >= mapa[posicion[0]][posicion[1]]:
            es_visible = False
            break
    return es_visible, count

def visible_desde_abajo(posicion, mapa):
    es_visible = True
    count = 0
    for i in range(posicion[0] + 1, len(mapa)):
        count += 1
        if mapa[i][posicion[1]] >= mapa[posicion[0]][posicion[1]]:
            es_visible = False
            break
    return es_visible, count

def visible_desde_derecha(posicion, mapa):
    es_visible = True
    count = 0
    for i in range(posicion[1] + 1, len(mapa[0])):
        count += 1
        if mapa[posicion[0]][i] >= mapa[posicion[0]][posicion[1]]:
            es_visible = False
            break
    return es_visible, count

def visible_desde_izquierda(posicion, mapa):
    es_visible = True
    count = 0
    for i in range(posicion[1] - 1, -1, -1):
        count += 1
        if mapa[posicion[0]][i] >= mapa[posicion[0]][posicion[1]]:
            es_visible = False
            break
    return es_visible, count

#---------------------- FIN DECLARACIÓN DE FUNCIONES ---------------------------

#---------------------- INICIO DEL PROGRAMA ---------------------------
with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [x[:-1] for x in lines]

arboles_en_bordes = 2*len(lines[0]) + 2*(len(lines) - 2)
total_visibles = arboles_en_bordes
num_max = 0

for i in range(1, len(lines) - 1):
    for j in range(1, len(lines[0]) - 1):
        posicion = [i,j]
        bol_abajo, num_abajo = visible_desde_abajo(posicion, lines)
        bol_arriba, num_arriba = visible_desde_arriba(posicion, lines)
        bol_derecha, num_derecha = visible_desde_derecha(posicion, lines)
        bol_izquierda, num_izquierda = visible_desde_izquierda(posicion, lines)

        if bol_abajo or bol_arriba or bol_derecha or bol_izquierda:
            total_visibles += 1
            scenic_score = num_abajo*num_arriba*num_derecha*num_izquierda
            if(num_max < scenic_score):
                num_max = scenic_score

print('En total hay',total_visibles,'árboles visibles')
print('Max scenic score:', num_max)
