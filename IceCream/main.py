from pprint import pprint
from sys import argv
from collections import Counter
ONE = "1"
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
class Flavor:
    def __init__(self):
        self.wants = Counter()
    def all_malted(self):
        return self.wants[1] and not self.wants[0]
    def all_unmalted(self):
        return self.wants[0] and not self.wants[1]
    def add(self, element):
        self.wants.update([element])
def test(customers, list):
    for i in customers:
        if not i.test(list):
            return False
    return True
with open(argv[1]) as f:
    with open("output.txt", 'w') as w:
        for i in range(int(f.readline())):
            flavors = int(f.readline())
            num_customers = int(f.readline())
            customers = []
            for _ in range(num_customers):
                customers.append(Customer(f.readline()))
            wants = {p:Flavor() for p in range(flavors)}
            for customer in customers:
                for flavor, way in customer.likes.items():
                    wants[flavor].add(int(way))
            worked = False
            for curr in range(2**flavors):
                currlist = [int(bool(curr & 2**p)) for p in range(flavors)]
                if test(customers, currlist):
                    w.write("Case #{}: {}\n".format(i + 1, " ".join((str(q) for q in currlist))))
                    worked = True
                    break
            if not worked:
                w.write("Case #{}: IMPOSSIBLE\n".format(i + 1))
            print("Did one")