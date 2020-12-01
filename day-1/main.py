def part_one(array):
    for x in array:
        for y in array:
            if((x+y) == 2020):
                print("[!] FOUND: " + str(x) + " AND " + str(y))
                solution = x * y
                print("SOLUTION: " + str(solution))
                return(solution)

def part_two(array):
    for x in array:
        for y in array:
            for z in array:
                if((x+y+z) == 2020):
                    print("[!] FOUND: " + str(x) + ", " + str(y) + " AND " + str(z))
                    solution = x * y * z
                    print("SOLUTION: " + str(solution))
                    return(solution)

if __name__ == "__main__":
    f = open("input.txt", "r")
    array:int = []
    for number in f:
        array.append(int(number))
        
    part_one(array)
    part_two(array)