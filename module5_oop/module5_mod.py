class IntegerStore:
    def __init__(self):
        self.nums = []

    def add_num(self, num):
        self.nums.append(num)

    def find_num(self, target):
        if target in self.nums:
            return self.nums.index(target) + 1 #1 indexed
  
        return -1
