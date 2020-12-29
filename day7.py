file = open("input.txt", 'r')
line = file.readline()
rules = []
bags = []

while line:
    rules.append(line)
    line = file.readline()
for x in rules:
    contain = x.find("contain")
    if x.find("shiny gold",contain) != -1:
        bag = ""
        y = 0
        while bag.find("bag") == -1:
            bag = bag + x[y]
            y = y + 1
        bags.append(bag)
for y in bags:
    for x in rules:
        contain = x.find("contain")
        if x.find(y,contain) != -1:
            bag = ""
            z = 0
            while bag.find("bag") == -1:
                bag = bag + x[z]
                z = z + 1
            if(bag not in bags):
                bags.append(bag)

#print(bags)
print(len(bags))


file.close()