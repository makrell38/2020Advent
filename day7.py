file = open("input.txt", 'r')
line = file.readline()
rules = []
bags = []

while line:
    rules.append(line)
    line = file.readline()
#for part 1
#for x in rules:
#    contain = x.find("contain")
#    if x.find("shiny gold",contain) != -1:
#        bag = ""
#        y = 0
#        while bag.find("bag") == -1:
#            bag = bag + x[y]
#            y = y + 1
#        bags.append(bag)
#for y in bags:
#    for x in rules:
#        contain = x.find("contain")
#        if x.find(y,contain) != -1:
#            bag = ""
#            z = 0
#            while bag.find("bag") == -1:
#                bag = bag + x[z]
#                z = z + 1
#            if(bag not in bags):
#                bags.append(bag)

gold = ""
x = 0
while gold == "":
    if rules[x].find("shiny gold",0, 11) != -1:
        gold = rules[x]
    x = x + 1
contain = gold.find("contain")
bag = ""
z = contain + len("contain") - 1
while gold[z] != '.':
    bag = ""
    num = z + 2
    if gold[num] != 'n':
        z = num+2
        while bag.find("bag") == -1:
            bag = bag + gold[z]
            z = z + 1
        if(bag not in bags):
            for i in range(0,int(gold[num])):
                bags.append(bag)
        while gold[z] != ',' and gold[z] != '.':
            z = z + 1
search= ""
for k in bags:
    search = ""
    x = 0
    while search == "":
        contain = rules[x].find("contain")
        if rules[x].find(k,0, contain) != -1:
            search = rules[x]
        x = x + 1
    bag = ""
    z = contain + len("contain") - 1
    con = True
    while con and search[z] != '.':
        bag = ""
        num = z + 2
        if search[num] != 'n':
            z = num+2
            while bag.find("bag") == -1:
                bag = bag + search[z]
                z = z + 1
            #if(bag not in bags):
            for i in range(0,int(search[num])):
                bags.append(bag)
            while search[z] != ',' and search[z] != '.':
                z = z + 1
        else:
            con = False

#print(bags)
print(len(bags))


file.close()