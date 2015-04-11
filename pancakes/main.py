from sys import argv
from functools import reduce
from pprint import pprint
def steps(diners):
    out = 0
    while max(diners) != 0:
        if diners[0] % 2 == 0 and diners[0] > 2:
            newlist = diners
            diners[0] /= 2
            diners.append(diners[0])
            newlist, diners = sorted(diners, reverse=True), newlist
            if steps(sorted(newlist, reverse=True)) <= steps(diners):
                out += 1
                return out + steps(sorted(newlist, reverse=True))
            else:
                diners = list(map(lambda x: x-1, diners))
            out += 1
        elif diners[0] <= 2:
            out += diners[0]
            break
        else:
            diners = list(map(lambda x: x-1, diners))
            out += 1
    return out
with open(argv[1]) as f:
    with open("output.txt", 'w') as w:
        for i in range(int(f.readline())):
            f.readline()
            diners = []
            minutes = 0
            for l in f.readline().split(" "):
                diners.append(int(l))
            diners.sort(reverse=True)
            minutes = steps(diners)
            # while max(diners) != 0:
                # minutes += 1
                # special = False
                # if diners[0] % 2 == 0 and diners[0] > 2:
                    # special = True
                    # diners[0] /= 2
                    # diners.append(diners[0])
                    # diners.sort(reverse=True)
                # if special:
                    # continue
                # else:
                    # diners = list(map(lambda x: x-1 if x > 0 else 0, diners))
            w.write("Case #{}: {}\n".format(i + 1, int(minutes)))