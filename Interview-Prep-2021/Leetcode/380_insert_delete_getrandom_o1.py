# LINK: https://leetcode.com/problems/insert-delete-getrandom-o1/

class RandomizedSet(object):

    def __init__(self):
        self.ind = {}
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
        
        i = self.ind[val]
        self.ind[self.values[-1]] = i
        self.values[i] = self.values[-1]
        
        self.ind.pop(val)
        self.values.pop()
        return True

    def getRandom(self):
        return random.choice(self.values)
        
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
