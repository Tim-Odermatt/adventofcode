import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))

test
part1 = 0
part2 = 0
output1 = []
output2 = []
# x stays undefined
# y stays undefined
# z stays undefined


INPUT_STRING = open("puzzle_input.txt", "r").read()
checkString = ""
doindexer = "+"

def validateAndCalculate(INPUT, start):
    x = 0
    y = 0
    number1 = ""
    number2 = ""
    while INPUT[start+x].isdigit() and x < 3:
        number1 += str(INPUT[start+x])
        x += 1
    if INPUT[start+x] == ",":
        x += 1
        while INPUT[start+x+y].isdigit() and y < 3:
            number2 += str(INPUT[start+x+y])
            y += 1
        if INPUT[start+x+y] == ")":
            output = int(number1)*int(number2)
            return output


for x in range(len(INPUT_STRING)): #len(INPUT_STRING)
    if INPUT_STRING.find("do()",x) == x:
        doindexer = "+"
    elif INPUT_STRING.find("don't()",x) == x:
        doindexer = "-"
    checkString += str(doindexer)


for x in range(len(INPUT_STRING)): #len(INPUT_STRING)
    if INPUT_STRING.find("mul(",x) == x:
        validater = validateAndCalculate(INPUT_STRING, x+4)
        if validater != None:
            output1.append(validater)
        if checkString[x] == "+":
            validater = validateAndCalculate(INPUT_STRING, x+4)
            if validater != None:
                output2.append(validater)


part1 = sum(output1)
part2 = sum(output2)
print(f"part 1 = {part1}")
print(f"part 2 = {part2}")