def part_one(matrix):
    counter = 0
    column = 0
    line = 0
    
    while line < len(matrix):
        if matrix[line][column%len(matrix[line])] == "#":
            counter += 1
        column += 3
        line += 1

    print("[!] SOLVED: The solution for part one is: " + str(counter))

def part_two(matrix):
    slopes = [(1,1),(3,1),(5,1),(7,1),(1,2)]
    result: int = 1

    for (jump_column, jump_line) in slopes:
        column = 0
        line = 0
        counter = 0
        while line < len(matrix):
            if matrix[line][column%len(matrix[line])] == "#":
                counter += 1
            column += jump_column
            line += jump_line
        result *= counter

    print("[!] SOLVED: The solution for part two is: " + str(result))

    

if __name__ == "__main__":
    f = open("input.txt", "r")
    matrix: str = []
    for lines in f:
        elements = lines.rstrip('\n')
        matrix.append(list(elements.strip()))

    part_one(matrix)
    part_two(matrix)