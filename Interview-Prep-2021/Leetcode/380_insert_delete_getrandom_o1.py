# LINK: https://leetcode.com/problems/insert-delete-getrandom-o1/

# Topic: Array
# This is an Array, Hash Table, Math, Design, or Randomized problem.

# TC: O(1)
# SC: O(N)

class RandomizedSet(object):
    def __init__(self):
        self.ind = {}
        # TRICK: The 'self.values' has to be a list.
        self.values = []
        
    def insert(self, val):
        if val in self.ind:
            return False
        
        self.values.append(val)
        self.ind[val] = len(self.values)-1
        return True

    def remove(self, val):
        if val not in self.ind:
            return False

        # TRICK: With remove(), we have a four step process:
        # 1) Get the index of val (i).
        # 2) Set the index of the last value in the array to i.
        # 3) Set the ith value in the array to the last value.
        # 4) Pop val from the indices; pop the last value from the array.
        
        i = self.ind[val]
        self.ind[self.values[-1]] = i
        self.values[i] = self.values[-1]
        
        self.ind.pop(val)
        self.values.pop()
        return True

    def getRandom(self):
        # TRICK: The trick here is 'random.choice(self.values)'.
        return random.choice(self.values)
        
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
