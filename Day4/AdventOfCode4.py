with open('input.txt', 'r') as f:
    lines = f.readlines()

lines = [x[:-1] for x in lines]
count = 0
count2 = 0

for l in lines:
    elfos = l.split(',')
    elf1 = elfos[0].split('-')
    elf2 = elfos[1].split('-')
    elf1 = set([i for i in range(int(elf1[0]), int(elf1[1]) + 1)])
    elf2 = set([i for i in range(int(elf2[0]), int(elf2[1]) + 1)])

    if elf1.issubset(elf2) or elf2.issubset(elf1):
        count += 1

    if elf1.intersection(elf2):
        count2 += 1

print('Ejercicio 1: ', count)
print('Ejercicio 2: ', count2)
