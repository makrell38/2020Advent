#does one too many correct 
file = open("input.txt", 'r')
check = True
count = 0
num = 0
while check:
    pp = ""
    line = file.readline()
    if not line:
        check = False
    else:
        num = num + 1
        valid = 1
        nlines = 0 
        pp = pp + line
        while nlines < 1 and line:
            line = file.readline()
            if line == '\n':
                nlines = nlines + 1
            elif not line:
                pp = pp + '\n'
            else:
                pp = pp + line
        if pp.find("byr") != -1 and pp.find("iyr") != -1 and pp.find("eyr") != -1 and pp.find("hgt") != -1 and pp.find("hcl") != -1 and pp.find("ecl") != -1 and pp.find("pid") != -1:
            #count = count + 1
            valid = 1

            #birth year
            val = ""
            loc = 0 
            x = pp.find("byr")+4
            while pp[x] != ' ' and pp[x] != '\n':
                val = val + pp[x]
                x = x + 1
                loc = loc + 1
            if loc != 4:
                valid = 0
                #print("bry l")
            byr = int(val)
            if byr < 1920 or byr > 2002:
                #print("byr")
                valid = 0

            #issue year
            val = ""
            loc = 0
            x = pp.find("iyr")+4
            while pp[x] != ' ' and pp[x] != '\n':
                val = val + pp[x]
                x = x + 1
                loc = loc + 1
            if loc != 4:
                valid = 0
                #print("iyr l")
            iyr = int(val)
            if iyr < 2010 or iyr > 2020:
                valid = 0
                #print("iyr")

            #expiration year
            val = ""
            loc = 0
            x = pp.find("eyr")+4
            while pp[x] != ' ' and pp[x] != '\n':
                val = val + pp[x]
                x = x + 1
                loc = loc + 1
            if loc != 4:
                valid = 0
                #print("eyr l")
            eyr = int(val)
            if eyr < 2020 or eyr > 2030:
                valid = 0
                #print("eyr")
            
            #height
            val = ""
            x = pp.find("hgt")+4
            while pp[x] != ' ' and pp[x] != '\n':
                val = val + pp[x]
                x = x + 1
            height = ""
            if val.find("cm") != -1:
                for y in range(0, len(val)-2):
                    height = height + val[y]
                if int(height) < 150 or int(height) > 193:
                    #print("hgt cm")
                    valid = 0
            elif val.find("in") != -1:
                for y in range(0, len(val)-2):
                    height = height + val[y]
                if int(height) < 59 or int(height) > 76:
                    valid = 0
                    #print("hgt in")
            else:
                valid = 0
                #print("hgt")


            #hair color
            val = ""
            loc = 0
            if pp[pp.find("hcl")+4] != '#':
                valid = 0
                #print("hcl #")
            else:
                x = pp.find("hcl")+5
                while pp[x] != ' ' and pp[x] != '\n':
                    if pp[x] < '0' or (pp[x] > '9' and pp[x] < 'a') or pp[x] > 'f':
                        valid = 0
                        #print("hcl")
                    x = x + 1
                    loc = loc + 1
                if loc != 6:
                    valid = 0
                    #print("hcl big")
            
            #eye color
            val = ""
            loc = 0
            x = pp.find("ecl")+4
            while pp[x] != ' ' and pp[x] != '\n':
                val = val + pp[x]
                x = x + 1
                loc = loc + 1
            if loc != 3:
                valid = 0
                #print("ecl l")
            elif val.find("amb") != -1 and val.find("blu") != -1 and val.find("gry") != -1 and val.find("grn") != -1 and val.find("hzl") != -1 and val.find("oth") != -1:
                valid = 0
                #print("ecl")
            
            #passport id
            val = ""
            loc = 0
            x = pp.find("pid")+4
            while pp[x] != ' ' and pp[x] != '\n':
                val = val + pp[x]
                if pp[x] < '0' or pp[x] > '9':
                    valid = 0
                    #print("pid")
                x = x + 1
                loc = loc + 1
            if loc != 9:
                valid = 0
                #print("pid l")
            
        
        else:
            valid = 0
            #print("missing")

        if valid == 1:
            count = count + 1
            print(num)
            
print(count)


file.close()