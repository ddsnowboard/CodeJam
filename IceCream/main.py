from sys import argv
from collections import Counter
from time import clock
ONE = "1"
WORKS = "works"
CONTINUE = "cont"
clock()
class Customer:
    def __init__(self, list):
        self.original_list = list
        nums = list.split(" ")
        self.likes = {}
        for i in range(1, len(nums), 2):
            self.likes[int(nums[i])-1] = nums[i+1].strip() == ONE
    def __str__(self):
        return str(list(self.likes.items()))
    def test(self, list):
        for i, j in enumerate(list):
            if self.likes.get(i, -1) == j:
                return True
        return False
    def malted_wants(self):
        return [i for i, j in self.likes.items() if j == 1]
def test(customers, list):
    for customer in customers:
        if not customer.test(list):
            return customer
    return WORKS
with open(argv[1]) as f:
    with open("output.txt", 'w') as w:
        for i in range(int(f.readline())):
            num_flavors = int(f.readline())
            num_customers = int(f.readline())
            customers = []
            starting_list = [0] * num_flavors
            for _ in range(num_customers):
                customers.append(Customer(f.readline()))
            currlist = starting_list
            # Result will either be WORKS, which indicates success, or a Customer object, which indicates failure, with the
            # indicated customer being unhappy. 
            result = test(customers, currlist)
            while result != WORKS and result != CONTINUE:
                desires = result.malted_wants()
                counter = 0
                this_try = currlist
                try:
                    this_try[desires[counter]] = 1
                except IndexError:
                    w.write("Case #{}: IMPOSSIBLE\n".format(i + 1))
                    result = CONTINUE
                    continue
                while test(customers, currlist) == result:
                    counter += 1
                    this_try = currlist
                    this_try[desires[counter]] = 1
                currlist = this_try
                result = test(customers, currlist)
            if result == WORKS:
                w.write("Case #{}: {}\n".format(i + 1, " ".join((str(l) for l in currlist))))
print(clock())