with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [x[:-1] for x in lines]
nlines = len(lines)
puntuacion = 0

for i in range(0, nlines, 3):
    elf1 = set(lines[i])
    elf2 = set(lines[i+1])
    elf3 = set(lines[i+2])

    comun = elf1.intersection(elf2.intersection(elf3))
    for c in comun:
        if c.isupper():
            puntuacion += ord(c) - 38
        else:
            puntuacion += ord(c) - 96

print(puntuacion)
