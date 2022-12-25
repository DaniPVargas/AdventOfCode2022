with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [x[:-1] for x in lines]

ciclos = 0
X = 1
actualizarX = False

ciclos_signal = [20, 60, 100, 140, 180, 220]
sum_strength = 0
dibujo = []

for instruccion in lines:
    if instruccion.startswith('addx'):
        actualizarX = True
        #Avanzamos dos ciclos y comprobamos si se calcula la fuerza de la señal.
        for i in range(2):
            if abs(ciclos%40 - X) <= 1:
                dibujo.append('#')
            else:
                dibujo.append('.')
            ciclos += 1
            if ciclos in ciclos_signal:
                sum_strength += ciclos*X

    if instruccion.startswith('noop'):
        if abs(ciclos%40 - X) <= 1:
            dibujo.append('#')
        else:
            dibujo.append('.')
        ciclos += 1
        if ciclos in ciclos_signal:
            sum_strength += ciclos*X

    if actualizarX:
        X += int(instruccion.split()[1])
        actualizarX = False

print(sum_strength,'\n')

print(''.join(dibujo[0:40]))
print(''.join(dibujo[40:80]))
print(''.join(dibujo[80:120]))
print(''.join(dibujo[120:160]))
print(''.join(dibujo[160:200]))
print(''.join(dibujo[200:240]))
