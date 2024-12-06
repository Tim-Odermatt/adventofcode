import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


part1 = 0
part2 = 0
output1 = []
output2 = []
# w stays undefined
# x stays undefined
# y stays undefined
# z stays undefined


INPUT_STRING = open("puzzle_input.txt", "r").read()

def turn90degree(pointer):
    global turns
    turns += 1
    if pointer == ">":
        return "v"
    elif pointer == "v":
        return "<"
    elif pointer == "<":
        return "^"
    elif pointer == "^":
        return ">"

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

turns = 0
horizontal = INPUT_STRING.split()
vertical = makeVertical(horizontal)
finished1 = False
#for w in range(500):
while not finished1:
    for x in range(len(horizontal)):
        if horizontal[x].find(">") != -1:
            atSlice = x
            positionPointer = horizontal[atSlice].find(">")
            horizontalArray = list(horizontal[atSlice])
            if horizontal[atSlice].find("#", positionPointer, -1) == -1:
                finished1 = True
            positionBarrel = horizontal[atSlice].find("#", positionPointer, -1)
            for y in range(positionPointer, positionBarrel, 1):
                horizontalArray[y] = "X"
            horizontalArray[positionBarrel-1] = turn90degree(horizontal[atSlice][positionPointer])
            horizontal[atSlice] = "".join(horizontalArray)
            vertical = makeVertical(horizontal)
            break

        elif horizontal[x].find("v") != -1:
            positionPointer = x
            atSlice = horizontal[x].find("v")
            vertcalArray = list(vertical[atSlice])
            positionBarrel = vertical[atSlice].find("#", positionPointer, -1)
            if vertical[atSlice].find("#", positionPointer, -1) == -1:
                finished1 = True
                positionBarrel = -1
            for y in range(positionPointer, positionBarrel, 1):
                vertcalArray[y] = "X"
            vertcalArray[positionBarrel-1] = turn90degree(vertical[atSlice][positionPointer])
            if finished1:
                vertcalArray[positionBarrel+1] = "X"
            
            vertical[atSlice] = "".join(vertcalArray)
            horizontal = makeVertical(vertical)
            break

        elif horizontal[x].find("<") != -1:
            atSlice = x
            positionPointer = horizontal[atSlice].find("<")
            horizontalArray = list(horizontal[atSlice])
            positionBarrel = horizontal[atSlice].rfind("#", 0, positionPointer)
            if horizontal[atSlice].rfind("#", 0, positionPointer) == -1:
                finished1 = True
                positionBarrel = -1
            for y in range(positionBarrel+1, positionPointer+1, 1):
                horizontalArray[y] = "X"
            horizontalArray[positionBarrel+1] = turn90degree(horizontal[atSlice][positionPointer])
            if finished1:
                horizontalArray[positionBarrel+1] = "X"
            horizontal[atSlice] = "".join(horizontalArray)
            vertical = makeVertical(horizontal)
            break

        elif horizontal[x].find("^") != -1:
            positionPointer = x
            atSlice = horizontal[x].find("^")
            vertcalArray = list(vertical[atSlice])
            positionBarrel = vertical[atSlice].rfind("#", 0, positionPointer)
            if vertical[atSlice].rfind("#", 0, positionPointer) == -1:
                finished1 = True
                positionBarrel = 0
            for y in range(positionBarrel+1, positionPointer+1, 1):
                vertcalArray[y] = "X"
            vertcalArray[positionBarrel+1] = turn90degree(vertical[atSlice][positionPointer])
            vertical[atSlice] = "".join(vertcalArray)
            horizontal = makeVertical(vertical)
            break

for x in range(len(horizontal)):
    output1.append(horizontal[x].count("X"))
    print(horizontal[x])


def check(horizontal):
    vertical = makeVertical(horizontal)
    for w in range(200):
        for x in range(len(horizontal)):
            if horizontal[x].find(">") != -1:
                atSlice = x
                positionPointer = horizontal[atSlice].find(">")
                horizontalArray = list(horizontal[atSlice])
                if horizontal[atSlice].find("#", positionPointer, -1) == -1:
                    return True
                positionBarrel = horizontal[atSlice].find("#", positionPointer, -1)
                for y in range(positionPointer, positionBarrel, 1):
                    horizontalArray[y] = "X"
                horizontalArray[positionBarrel-1] = turn90degree(horizontal[atSlice][positionPointer])
                horizontal[atSlice] = "".join(horizontalArray)
                vertical = makeVertical(horizontal)
                break

            elif horizontal[x].find("v") != -1:
                positionPointer = x
                atSlice = horizontal[x].find("v")
                vertcalArray = list(vertical[atSlice])
                positionBarrel = vertical[atSlice].find("#", positionPointer, -1)
                if vertical[atSlice].find("#", positionPointer, -1) == -1:
                    return True
                for y in range(positionPointer, positionBarrel, 1):
                    vertcalArray[y] = "X"
                vertcalArray[positionBarrel-1] = turn90degree(vertical[atSlice][positionPointer])
                if finished1:
                    vertcalArray[positionBarrel+1] = "X"
                vertical[atSlice] = "".join(vertcalArray)
                horizontal = makeVertical(vertical)
                break

            elif horizontal[x].find("<") != -1:
                atSlice = x
                positionPointer = horizontal[atSlice].find("<")
                horizontalArray = list(horizontal[atSlice])
                positionBarrel = horizontal[atSlice].rfind("#", 0, positionPointer)
                if horizontal[atSlice].rfind("#", 0, positionPointer) == -1:
                    return True
                for y in range(positionBarrel+1, positionPointer+1, 1):
                    horizontalArray[y] = "X"
                horizontalArray[positionBarrel+1] = turn90degree(horizontal[atSlice][positionPointer])
                if finished1:
                    horizontalArray[positionBarrel+1] = "X"
                horizontal[atSlice] = "".join(horizontalArray)
                vertical = makeVertical(horizontal)
                break

            elif horizontal[x].find("^") != -1:
                positionPointer = x
                atSlice = horizontal[x].find("^")
                vertcalArray = list(vertical[atSlice])
                positionBarrel = vertical[atSlice].rfind("#", 0, positionPointer)
                if vertical[atSlice].rfind("#", 0, positionPointer) == -1:
                    return True
                for y in range(positionBarrel+1, positionPointer+1, 1):
                    vertcalArray[y] = "X"
                vertcalArray[positionBarrel+1] = turn90degree(vertical[atSlice][positionPointer])
                vertical[atSlice] = "".join(vertcalArray)
                horizontal = makeVertical(vertical)
                break
            else:
                return True
    return False

listA = horizontal[:]
for x in range(len(listA)):
    for y in range(len(listA[x])):
        if listA[x][y] == "X" and [x, y] != [90, 66] :
            listB = INPUT_STRING.split()
            array = list(listA[x])
            #print()
            #print(listB[x])
            array[y] = "#"
            listB[x] = "".join(array)
            #print(listB[x])
            if not check(listB):
                part2 += 1
                print(part2)




print(turns)
part1 = sum(output1)
#part2 = sum(output2)
print(f"part 1 = {part1}")
print(f"part 2 = {part2}")