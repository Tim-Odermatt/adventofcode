import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


input = open("puzzle_input.txt", "r").read()
inputArray = input.split()
arr1 = []
arr2 = []
output = 0
x = 0
while x < 2000:
    arr1.append(inputArray[int(x)])
    arr2.append(inputArray[int(x+1)])
    x += 2
arr1sort = sorted(arr1)
arr2sort = sorted(arr2)
x = 0
while x < 1000:
    output += abs(int(arr1sort[int(x)])-int(arr2sort[int(x)]))
    x += 1
print(f"part 1 = {output}")

output = 0
x = 0
while x < 1000:
    y = 0
    z = 0
    while y < 1000:
        if arr1[x] == arr2[y]:
            z += 1
        y += 1
    output += int(arr1[x])*z
    x += 1
print(f"part 2 = {output}")