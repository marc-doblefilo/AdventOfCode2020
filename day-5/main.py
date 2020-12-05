import math

def part_one(seats):
    highest_seatID: int = 0
    for seat in seats:
        min: int = 0
        max: int = 127
        min_column: int = 0
        max_column: int = 7
        row: int = 0
        column: int = 0
        seatID: int = 0
        for char in seat[0 : 7]:
            if char == "F":
                max = math.floor((max+min) / 2)
            if char == "B":
                min = math.ceil((max+min) / 2)
        for char in seat[7 : 10]:
            if char == "L":
                max_column = math.floor((max_column+min_column) / 2)
            if char == "R":
                min_column = math.ceil((max_column+min_column) / 2)
        
        if(seat[6] == "F"):
            row = min
        if(seat[6] == "B"):
            row = max
        if(seat[9] == "L"):
            column = min_column
        if(seat[9] == "R"):
            column = max_column
        
        seatID = row * 8 + column

        if seatID > highest_seatID:
            highest_seatID = seatID

    print("[!] SOLVED: The solution for part one is: " + str(highest_seatID))
    return(highest_seatID)

def part_two(seats):
    IDs = []
    
    for seat in seats:
        min: int = 0
        max: int = 127
        min_column: int = 0
        max_column: int = 7
        row: int = 0
        column: int = 0
        seatID: int = 0
        for char in seat[0 : 7]:
            if char == "F":
                max = math.floor((max+min) / 2)
            if char == "B":
                min = math.ceil((max+min) / 2)
        for char in seat[7 : 10]:
            if char == "L":
                max_column = math.floor((max_column+min_column) / 2)
            if char == "R":
                min_column = math.ceil((max_column+min_column) / 2)
        
        if(seat[6] == "F"):
            row = min
        if(seat[6] == "B"):
            row = max
        if(seat[9] == "L"):
            column = min_column
        if(seat[9] == "R"):
            column = max_column
        
        seatID = row * 8 + column
        IDs.append(seatID)
    
    for id in IDs:
        if id+1 not in IDs and id+2 in IDs:
            missing = id + 1
            

    print("[!] SOLVED: The solution for part two is: " + str(missing))


if __name__ == "__main__":
    f = open("input.txt", "r")
    output: str = f.read()
    boarding_passes = output.split("\n")

    part_one(boarding_passes)
    part_two(boarding_passes)