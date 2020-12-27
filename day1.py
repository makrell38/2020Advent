entry = []
found = []
file = open('input.txt', 'r')
check = True
#to read in all inputs from file
while check:
    input = file.readline()
    if not input:
        check = False
    else:
        entry.append(int(input))
for x in entry:
    temp = 2020-x
    for y in entry:
        if y != x:
            temp2 = temp - y
            if temp2 in entry:
                #to make sure no double answers are found
                if x not in found and y not in found and temp2 not in found:
                    found.append(x)
                    found.append(y)
                    found.append(temp2)
                    print(x*y*temp2)