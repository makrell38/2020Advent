file = open("input.txt", 'r')
check = True
count = 0
while check:
    pp = ""
    line = file.readline()
    if not line:
        check = False
    else:
        nlines = 0 
        pp = pp + line
        while nlines < 1 and line:
            line = file.readline()
            if line == '\n':
                nlines = nlines + 1
            else:
                pp = pp + line
        if pp.find("byr") != -1 and pp.find("iyr") != -1 and pp.find("eyr") != -1 and pp.find("hgt") != -1 and pp.find("hcl") != -1 and pp.find("ecl") != -1 and pp.find("pid") != -1:
            count = count + 1
print(count)


file.close()