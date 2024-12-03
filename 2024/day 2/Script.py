import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


part1 = 0 
part2 = 0
# x stays undefined
# y stays undefined
# z stays undefined


INPUT_ARRAY = open("puzzle_input.txt", "r").read().splitlines()
for x in range(len(INPUT_ARRAY)):
    INPUT_ARRAY[x] = INPUT_ARRAY[x].split()
    for y in range(len(INPUT_ARRAY[x])):
        INPUT_ARRAY[x][y] = int(INPUT_ARRAY[x][y])


def array(input): #checks if a array has only increasing/decreasing nummber by 1, 2, 3  [65 67 70 72 74 73]
    output = []
    if input[0]-input[1] in (1, 2, 3):
        for x in range(len(input)-1):
            if input[x]-input[x+1] in (1, 2, 3):
                output.append(True) # [True, True, True, False]
            else:
                output.append(False)
                break
    elif input[0]-input[1] in (-1, -2, -3):
        for x in range(len(input)-1):
            if input[x]-input[x+1] in (-1, -2, -3):
                output.append(True)
            else:
                output.append(False)
                break
    else:
        output.append(False)
    if all(output) == True:
        return True


def stepper(INPUT_ARRAY, part):
    ouput = 0
    for x in range(len(INPUT_ARRAY)):  #range(1) len(INPUT_ARRAY)
        if array(INPUT_ARRAY[x]) == True:
            ouput += 1
        elif part == True:
            for y in range(len(INPUT_ARRAY[x])):
                z = INPUT_ARRAY[x][:]
                del z[y]
                #print(z)
                if array(z) == True:
                    ouput += 1
                    break
    return ouput


part1 = stepper(INPUT_ARRAY, False)
print(f"part 1 = {part1}")
part2 = stepper(INPUT_ARRAY, True)
print(f"part 2 = {part2}")