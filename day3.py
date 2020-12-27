file = open("input.txt", 'r')
check = True
loc = 0
num = 0
count = 0
total = []
line = file.readline()
length = len(line)
path = []
while check:
    line = file.readline()
    
    if not line:
        check = False
    else:
        num = num + 1
        path.append(line)
        #used in part 1
        #loc = (loc + 3)%(length-1)
        #if line[loc] == '#':
            #count = count + 1

for i in range(1,9,2):
    loc = 0
    count = 0
    for x in path:
        loc = (loc + i)%(length-1)
        if x[loc] == '#':
            count = count + 1
    total.append(count)

loc = 0
count = 0
for x in range(1,num+1,2):
    loc = (loc+1)%(length-1)
    if path[x][loc] == '#':
        count = count + 1
total.append(count)


final = 1
for y in total:
    final = final*y
print(final)

file.close()
