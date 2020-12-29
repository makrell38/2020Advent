def mySort(n):
    return len(n)

file = open("input.txt", 'r')
group = []
total = []
check = True
yes = 0
while check:
    line = file.readline()
    if not line: 
        check = False
        group[len(group)-1] = group[len(group)-1] +'\n'
    if line and line != '\n':
        group.append(line)
    else:
        group.sort(key=mySort)
        yes = len(group[0])-1
        for x in range(1,len(group)):
            for m in range(0,len(group[x])-1):
                add = True
                for y in range(0, x):
                    if group[y].find(group[x][m]) != -1:
                        add = False
                if add:
                    yes = yes + 1
        total.append(yes)
        group = []
        yes = 0
    

final = 0
for x in total:
    final = final + x
print(final)

file.close()