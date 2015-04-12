from sys import argv
from functools import reduce
DESIRED_OUTPUT = "ijk"
def xor(a, b):
    return (a or b) and not (a and b)
def quaternion(a, b):
    POSSIBILITIES = '1ijk'
    MAPPING = {'1': {'1':'1', 'i':'i', 'j':'j', 'k':'k'},
    'i':{'1':'i', 'i': '-1', 'j':'k', 'k':'-j'},
    'j':{'1':'j', 'i':'-k', 'j':'-1','k':'i'},
    'k':{'1':'k', 'i':'-k', 'j':'-i', 'k':'-1'}
    }
    negative = False
    if xor(a[0] == '-', b[0] == '-'):
        negative = True
        a = a.replace('-', '')
        b = b.replace('-', '')
    if not a in POSSIBILITIES or not b in POSSIBILITIES:
        raise Exception("Something bad happened; one of {} or {} is not valid".format(a, b))
    out = MAPPING[a][b]
    if negative:
        if out[0] == '-':
            return out[1:]
        else:
            return '-' + out
    return out
with open(argv[1]) as f:
    with open("output.txt", 'w') as w:
        for i in range(int(f.readline())):
            repetitions = int(f.readline().split(' ')[1])
            line = f.readline().strip() * repetitions
            # print(line)
            curr_idx = 1
            curr_tgt = 0
            found = True
            _ = 0
            while True:
                _ += 1
                if _ == 100:
                    _ = 0
                    print(curr_idx)
                print(line[:curr_idx])
                # print("Inputting {}: recieved {}".format(line[:curr_idx], reduce(quaternion, line[:curr_idx])))
                if curr_tgt == len(DESIRED_OUTPUT):
                    found = True
                    break
                if curr_idx == 1 and line[0] == DESIRED_OUTPUT[curr_tgt]:
                    line = line[1:]
                    curr_idx = 1
                    try:
                        curr_tgt += 1
                    except IndexError:
                        found = False
                        break
                elif curr_idx == 1:
                    curr_idx += 1
                    continue
                elif reduce(quaternion, line[:curr_idx]) == DESIRED_OUTPUT[curr_tgt]:
                    line = line[curr_idx:]
                    curr_tgt += 1
                    curr_idx = 1
                else:
                    if curr_idx >= len(line) - 2:
                        found = False
                        break
                    else:
                        curr_idx += 1
            if found:
                w.write("Case #{}: YES\n".format(i+1))
            else:
                w.write("Case #{}: NO\n".format(i+1))