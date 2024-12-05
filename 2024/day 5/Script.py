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


INPUT_STRING = open("puzzle_input.txt", "r").read().split()


def ordercheck(z, order, rules):
    if order[z+1] in rules[order[z]]:
        return True
    else:
        return False

def completecheck(order, rules):
    for z in range(len(order)-1):
        if ordercheck(z, order, rules):
            pass
        else:
            return False
    else:
        return True


rulesAfter = {}
rulesBevor = {}
x = 0
while len(INPUT_STRING[x]) < 6:
    rule = INPUT_STRING[x][0]+INPUT_STRING[x][1]
    after = INPUT_STRING[x][3]+INPUT_STRING[x][4]
    if rule in rulesAfter:
        rulesAfter[rule].append(after)
    else:
        rulesAfter.update({rule:[]})
        rulesAfter[rule].append(after)
    if after in rulesBevor:
        rulesBevor[after].append(rule)
    else:
        rulesBevor.update({after:[]})
        rulesBevor[after].append(rule)

    x += 1

for y in range(len(INPUT_STRING)-x): #len(INPUT_STRING)-x
    ordering = INPUT_STRING[x+y].split(",")
    for z in range(len(ordering)-1):
        if ordercheck(z, ordering, rulesAfter):
            pass
        else:
            reordering = ordering[:]
            while completecheck(reordering, rulesAfter) == False:
                for w in range(1, len(reordering)):
                    if not ordercheck(0, [reordering[w], (reordering[w-1])], rulesBevor):
                        reordering[w], reordering[w-1] = reordering[w-1], reordering[w]
            output2.append(int(reordering[int((len(reordering)-1)/2)]))
            break
    else:
         output1.append(int(ordering[int((len(ordering)-1)/2)]))


part1 = sum(output1)
part2 = sum(output2)
print(f"part 1 = {part1}")
print(f"part 2 = {part2}")