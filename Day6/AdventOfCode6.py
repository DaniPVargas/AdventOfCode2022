with open('input.txt', 'r') as f:
    lines = f.readlines()

letras = list(lines[0][:-1])
caracteres = []
count = 15

for i in range(14):
    caracteres.append(letras[i])

if(len(set(caracteres)) == 14):
    print('14')
else:
    for i in range(14, len(letras)):
        caracteres.pop(0)
        caracteres.append(letras[i])
        if(len(set(caracteres)) == 14):
            print(count)
            exit()
        count += 1
