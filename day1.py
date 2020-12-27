#part 1 done
entry = []
file = open('input.txt', 'r')
check = True
while check:
    input = file.readline()
    if not input:
        check = False
    else:
        entry.append(int(input))
print("hello")
for x in entry:
    temp = 2020-x
    if temp in entry:
        print(x*temp)
print("this")