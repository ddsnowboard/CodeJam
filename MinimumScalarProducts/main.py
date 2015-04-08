from itertools import permutations
from sys import argv
with open(argv[1], 'r') as f:
    with open("output.txt", 'w') as w:
        for i in range(int(f.readline())):
            f.readline()
            x_terms = sorted([int(p) for p in f.readline().split(" ")])
            y_terms = sorted([int(p) for p in f.readline().split(" ")], reverse=True)
            w.write("Case #{}: {}\n".format(i+1, sum((j*k for j, k in zip(x_terms, y_terms)))))