def part_one(array):
    counter: int = 0
    for password in array:
        decoded_string = password.split(" ")
        decoded_min_max = decoded_string[0].split("-")
        min: int = int(decoded_min_max[0])
        max: int = int(decoded_min_max[1])
        decoded_letter: str = decoded_string[1]
        key_letter = decoded_letter[0]
        decoded_password = decoded_string[2]
        password = decoded_password.rstrip('\n')
        counter_letter_in_password: int = 0

        for letter in password:
            if letter == key_letter:
                counter_letter_in_password += 1
        
        if min <= counter_letter_in_password and counter_letter_in_password <= max:
            counter += 1

    print("[!] SOLVED: The solution for part one is: " + str(counter))

def part_two(array):
    counter: int = 0
    for password in array:
        decoded_string = password.split(" ")
        decoded_characters = decoded_string[0].split("-")
        first_character: int = int(decoded_characters[0]) - 1
        second_character: int = int(decoded_characters[1]) - 1
        decoded_letter: str = decoded_string[1]
        key_letter = decoded_letter[0]
        decoded_password = decoded_string[2]
        password = decoded_password.rstrip('\n')

        if(key_letter == password[first_character] or key_letter == password[second_character]):
            if(key_letter != password[first_character] or key_letter != password[second_character]):
                counter += 1

    print("[!] SOLVED: The solution for part two is: " + str(counter))

if __name__ == "__main__":
    f = open("input.txt", "r")
    array: str = []
    for password in f:
        array.append(password)

    part_one(array)
    part_two(array)