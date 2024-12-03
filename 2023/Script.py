import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))
input = open("puzzle_input.txt", "r").read()
xnputArray = input.split()
inputArray = input.split()
x = 0

SEARCHLIST = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
outputArr = []
while x < 1000:
    t = 0
    while t < len(xnputArray[x]):
        for searchQuery in SEARCHLIST:
            position = xnputArray[x].find(searchQuery, t)
            if position != -1:
                #print(f"found {searchQuery} at {position}")
                outString = ""
                for y in range(len(xnputArray[x])):
                    if y == position:
                        outString += str(SEARCHLIST.index(searchQuery)+1)
                    else:
                        outString += inputArray[x][y]
                inputArray[x] = outString
        t += 1
        
    for y in range(len(inputArray[x])):
        if inputArray[x][y].isnumeric() == True:
            int1 = inputArray[x][y]
            break
    for y in range(len(inputArray[x])-1, -1, -1):
        if inputArray[x][y].isnumeric() == True:
            int2 = inputArray[x][y]
            break
    outputArr.append(int(int1+int2))
    x += 1
#print(inputArray)
print(sum(outputArr))