file = open('input.txt', 'r')
check = True
total = 0
while check:
    line = file.readline()
    if not line:
        check = False
    else:
        length = len(line)
        min = ""
        max = ""
        x = 0
        while line[x] != '-':
            min = min + line[x]
            x = x + 1
        x = x + 1
        while line[x] != ' ':
            max = max + line[x]
            x =  x + 1
        x = x + 1
        value = line[x]
        x = x + 2
        input = line[x:length-1]
            
        minVal = int(min)
        maxVal = int(max)
        amount = 0
        for x in input:
            if x == value:
                amount = amount + 1 
        if amount >= minVal and amount <= maxVal:
            #print(input)
            total = total + 1

print(total)

file.close()