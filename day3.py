file = open("input.txt", 'r')
check = True
loc = 0
count = 0
line = file.readline()
length = len(line)
while check:
    line = file.readline()
    if not line:
        check = False
    else:
        loc = (loc + 3)%(length-1)
        if line[loc] == '#':
            count = count + 1
        
print(count)


file.close()
