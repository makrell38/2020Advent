file = open("input.txt", 'r')
row = [0,127]
col = [0,7]
max = 0
line = file.readline()
while line and line != '\n':
    row = [0,127]
    col = [0,7]
    for x in range(0,6):
        if line[x] == 'F':
            row[1] = (row[1] - row[0])//2 + row[0]
        else:
            row[0] = (row[1] - row[0])//2 +row[0] + 1
    if line[6] == 'F':
        r = row[0]
    else:
        r = row[1]
    for x in range(7,9):
        if line[x] == 'R':
            col[0] = (col[1] - col[0])//2 + col[0] +1
        else:
            col[1] = (col[1] - col[0])//2 + col[0]
    if line[9] == 'R':
        c = col[1]
    else:
        c = col[0]
    val = r*8 + c
    if val > max:
        max = val
    line = file.readline()

print(max)

file.close()

