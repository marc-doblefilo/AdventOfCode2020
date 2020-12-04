import re

def verify_passport(passport):
    if passport.find("byr") != -1:
        if passport.find("iyr") != -1:
            if passport.find("eyr") != -1:
                if passport.find("hgt") != -1:  
                    if passport.find("hcl") != -1:
                        if passport.find("ecl") != -1:
                            if passport.find("pid") != -1:
                                return True
    return False

def part_one(passports):
    counter: int = 0
    for passport in passports:
        if verify_passport(passport) == True:
            counter += 1

    print("[!] SOLVED: The solution for part one is: " + str(counter))

def part_two(passports):
    counter: int = 0
    for passport in passports:
        verified: bool = True
        if verify_passport(passport) == True:
            dict_passport = dict(s.split(":", 1) for s in passport.split())
            for key, value in dict_passport.items():
                if key == "byr":
                    value = int(value)
                    if value < 1920 or value > 2002:
                        verified = False
                if key == "iyr":
                    value = int(value)
                    if value < 2010 or value > 2020:
                        verified = False
                if key == "eyr":
                    value = int(value)
                    if value < 2020 or value > 2030:
                        verified = False
                if key == "hgt":
                    if value[-2:] == "cm":
                        height = value.rstrip('cm')
                        height = int(height)
                        if height < 150 or height > 193:
                            verified = False
                    if value[-2:] == "in":
                        height = value.rstrip('in')
                        height = int(height)
                        if height < 59 or height > 76:
                            verified = False

                    if value[-2:] != "in" and value[-2:] != "cm":
                        verified = False
                if key == "hcl":
                    if value[0] == "#":
                        color = value[1:]
                        valid_chars = "0123456789abcdef"
                        valid_char: bool = False
                        if len(color) == 6:
                            for color_char in color:
                                for char in valid_chars:
                                    valid_char = False
                                    if char == color_char:
                                        valid_char = True
                                        break
                                if valid_char == False:
                                    verified = False
                                    break  
                        else:
                            verified = False
                    else:
                        verified = False
                if key == "ecl":
                    valid_colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                    valid_color: bool = False
                    for color in valid_colors:
                        if value == color:
                            valid_color = True

                    if valid_color == False:
                        verified = False
                if key == "pid":
                    if value.isdecimal() == False:
                        verified = False
                    if len(value) != 9:
                        verified = False
                                


            if verified == True:
                counter += 1
        
    
    print("[!] SOLVED: The solution for part two is: " + str(counter))

if __name__ == "__main__":
    f = open("input.txt", "r")
    output: str = f.read()
    passports = output.split("\n\n")

    part_one(passports)
    part_two(passports)