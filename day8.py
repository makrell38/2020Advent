file = open("input.txt", 'r')
instruc = []
acc = 0
line = file.readline()
while line:
    instruc.append(line)
    line = file.readline()
visit = [0] * len(instruc)
check = True
loc = 0
while check:
    if visit[loc] != 0:
        check = False
    else:
        visit[loc] = visit[loc] + 1
        x = 5
        value = ""
        while instruc[loc][x] != '\n':
            value = value + instruc[loc][x]
            x = x + 1
        if '-' in instruc[loc]:
            value = int(value) * (-1)
        if "acc" in instruc[loc]:
            acc = acc + int(value)
            loc = loc + 1
        elif "jmp" in instruc[loc]:
            loc = loc + int(value)
        else:
            loc = loc +1
print(acc)
