from sys import argv
# Can I use a greedy algorithm for this? I suppose I'll find out...
# Not quite.  
with open(argv[1], 'r') as f:
    with open("output.txt", 'w') as w:
        n = int(f.readline())
        for case in range(n):
            money = int(f.readline())
            out = []
            f.readline()
            products = [int(i) for i in f.readline().split(" ")]
            for i,j in enumerate(products):
                if j <= money:
                    if money-j in products:
                        if out:
                            print(out)
                            print(money)
                            print(j)
                            print(products)
                            assert False
                        try:
                            out.append([l if k != i else None for k, l in enumerate(products)].index(money-j))
                            out.append(i)
                        except ValueError:
                            continue
                        break
            w.write("Case #{}: {}\n".format(str(case+1), " ".join([str(i+1) for i in sorted(out)])))