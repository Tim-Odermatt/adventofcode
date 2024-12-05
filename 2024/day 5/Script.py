import os
os.chdir(os.path.dirname(os.path.abspath(__file__)))


part1 = 0
part2 = 0
output1 = []
output2 = []
# x stays undefined
# y stays undefined
# z stays undefined


INPUT_STRING = open("puzzle_input.txt", "r").read().split()


rulesAfter = {}
x = 0
while len(INPUT_STRING[x]) < 6:
    rule = INPUT_STRING[x][0]+INPUT_STRING[x][1]
    after = INPUT_STRING[x][3]+INPUT_STRING[x][4]
    if rule in rulesAfter:
        rulesAfter[rule].append(after)
    else:
        rulesAfter.update({rule:[]})
        rulesAfter[rule].append(after)

    x += 1

for y in range(len(INPUT_STRING)-x): #len(INPUT_STRING)-x
    ordering = INPUT_STRING[x+y].split(",")
    for z in range(len(ordering)-1):
        if ordering[z+1] in rulesAfter[ordering[z]]:
            #print(f"{ordering[z]} in {ordering[z+1]}")
            pass
        else:
            reordering = ordering
            output2.append(int(reordering[int((len(reordering)-1)/2)]))
            break
    else:
         output1.append(int(ordering[int((len(ordering)-1)/2)]))


part1 = sum(output1)
part2 = sum(output2)
print(f"part 1 = {part1}")
print(f"part 2 = {part2}")