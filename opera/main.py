from sys import argv
import re
with open(argv[1]) as f:
    with open("output.txt", 'w') as w:
        for i in range(int(f.readline())):
            nums = [int(p) for p in f.readline().split(" ")[1] if re.match("\d", p)]
            friends = 0
            standers = 0
            while True:
                for k, l in enumerate(nums):
                    if standers >= k:
                        standers += l
                if standers >= sum(nums) + friends:
                    break
                else:
                    friends += 1
                    standers = friends
            w.write("Case #{}: {}\n".format(i + 1, friends))