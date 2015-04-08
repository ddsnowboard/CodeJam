from sys import argv
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
def test(customers, list):
    # Make a function that tests a specific arrangement to see if it 
    # will satisfy everyone. 
with open(argv[1]) as f:
    with open("output.txt", 'w') as w:
        for i in range(int(f.readline())):
            flavors = int(f.readline())
            num_customers = int(f.readline())
            customers = []
            for i in range(num_customers):
                customers.append(Customer(f.readline()))
            