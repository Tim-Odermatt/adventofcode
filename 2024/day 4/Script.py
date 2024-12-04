import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


part1 = 0
part2 = 0
output1 = []
output2 = []
# x stays undefined
# y stays undefined
# z stays undefined


INPUT_STRING = open("puzzle_input.txt", "r").read()


def makeVertical(input):
    output = []
    string = ""
    for x in range(len(input[0])):
        for y in range(len(input)):
            if input[y][x] != " ":
                string += input[y][x]
        output.append(string)
        string = ""
    return output


def findXMAS(input):
    output = 0
    stepper = 0
    while len(input) > stepper:
        if input.find("XMAS", stepper) != -1 and (input.find("SAMX", stepper) == -1 or input.find("XMAS", stepper) < input.find("SAMX", stepper)):
            stepper = int(input.find("XMAS", stepper)+1)
            output += 1
        elif input.find("SAMX", stepper) != -1:
            stepper = input.find("SAMX", stepper)+1
            output += 1
        else:
            break
    return output


horizontal = INPUT_STRING.split()
vertical = makeVertical(horizontal)
diagonalleft = []
diagonalright = []


for x in range(len(horizontal)):
    for y in range(len(horizontal)):
        if 0 < x < len(horizontal)-1 and 0 < y < len(horizontal)-1:
            if horizontal[x][y] == "A":
                if horizontal[x-1][y-1] == "M" and horizontal[x+1][y+1] == "S":
                    if horizontal[x+1][y-1] == "M" and horizontal[x-1][y+1] == "S":
                        part2 += 1
                    elif horizontal[x-1][y+1] == "M" and horizontal[x+1][y-1] == "S":
                        part2 += 1
                elif horizontal[x+1][y+1] == "M" and horizontal[x-1][y-1] == "S":
                    if horizontal[x+1][y-1] == "M" and horizontal[x-1][y+1] == "S":
                        part2 += 1
                    elif horizontal[x-1][y+1] == "M" and horizontal[x+1][y-1] == "S":
                        part2 += 1


for x in range(len(horizontal)):
    diagonalleft.append(" "*x+horizontal[x]+" "*abs(int(x-len(horizontal)+1)))
    diagonalright.append(" "*abs(int(x-len(horizontal)+1))+horizontal[x]+" "*x)

diagonalleft = makeVertical(diagonalleft)
diagonalright = makeVertical(diagonalright)


for x in range(len(horizontal)):
    output1.append(findXMAS(horizontal[x]))
    output1.append(findXMAS(vertical[x]))
for x in range(len(diagonalleft)):
    output1.append(findXMAS(diagonalleft[x]))
    output1.append(findXMAS(diagonalright[x]))


part1 = sum(output1)
print(f"part 1 = {part1}")
print(f"part 2 = {part2}")