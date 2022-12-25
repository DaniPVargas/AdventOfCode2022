#------------------DECLARACION DE FUNCIONES------------------
def leer_ls_command(lines):
    elements = []
    while len(lines) > 0 and not lines[0].startswith('$'):
        elements.append(lines.pop(0))
    return elements, lines

def leer_contenido(contenido, list_ficheros):
    for x in contenido:
        if not x.startswith('dir'):
            list_ficheros.append(x)

def anadir_ficheros(directorios, list_ficheros, ruta_actual):
    for f in list_ficheros:
        for x in ruta_actual:
            if not x in directorios:
                directorios[x] = 0
            directorios[x] += int(f.split()[0])

#------------------FIN DECLARACION DE FUNCIONES------------------

#------------------DEFINICION OBJETO DIRECTORIO------------------

class dir:
    def __init__(self, nombre):
        self.nombre = nombre

#------------------ FIN DEFINICION OBJETO DIRECTORIO ------------------

#-------------------------- INICIO PROGRAMA --------------------------

with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [x[:-1] for x in lines]

command_cd = '$ cd '
command_cd_back = '$ cd ..'
command_list = '$ ls'

dic_directorios = {} #Diccionario con pares directorio-tamaño
dir_raiz = dir('/')
dic_directorios[dir_raiz] = 0
ruta_actual = []
ruta_actual.append(dir_raiz)

list_ficheros = []
lines.pop(0)

while len(lines) > 0:
    list_ficheros = []
    command = lines.pop(0)
    if command == command_list:
        contenido, lines = leer_ls_command(lines)
        leer_contenido(contenido, list_ficheros)
        if len(list_ficheros) > 0:
            anadir_ficheros(dic_directorios, list_ficheros, ruta_actual)
    if command == command_cd_back:
        ruta_actual.pop()
    if command.startswith(command_cd) and command != command_cd_back:
        newdir = dir(command.split()[-1])
        ruta_actual.append(newdir)

#Una vez tenemos los tamaños de todos los dic_directorios, calculamos al suma de los que tienen menos de 100000
suma = 0
for x in dic_directorios:
    if dic_directorios[x] <= 100000:
        suma += dic_directorios[x]

print('La solución de la primera parte es ', suma)

#---------------------------SEGUNDA PARTE DEL EJERCICIO---------------------------
total_space_available = 70000000
space_used = dic_directorios[dir_raiz]
actual_space_available = total_space_available - space_used
space_required = 30000000 - actual_space_available

posible_sizes = []

for x in dic_directorios:
    if dic_directorios[x] >= space_required:
        posible_sizes.append(dic_directorios[x])

print('La solucion de la segunda parte es ', min(posible_sizes))
