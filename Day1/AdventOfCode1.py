with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [x for x in lines]

calorias = []
elfo_actual = 0
top3 = 0

for num in lines:
    if num == '\n':
        calorias.append(elfo_actual)
        elfo_actual = 0
        continue
    elfo_actual += int(num)

calorias.append(elfo_actual)
print('El máximo es ', max(calorias))

for i in range(3):
    m = max(calorias)
    top3 += m
    calorias.remove(m)

print('La suma de los 3 elfos con más calorias es ', top3)
