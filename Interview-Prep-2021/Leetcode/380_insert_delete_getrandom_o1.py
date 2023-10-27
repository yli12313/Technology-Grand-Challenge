# LINK: https://leetcode.com/problems/insert-delete-getrandom-o1/

class RandomizedSet(object):
    # Constraints
    # - -2^31 <= val <= 2^31 - 1.
    # - At most 2 * 10^5 calls will be made to insert, remove, and getRandom.
    # - There will be at least one element in the data structure when getRandom is called.

    # Topic: Array
    # This is an Array, Hash Table, Math, Design or Randomized problem.

    # TC: O(1)
    # SC: O(N)

    def __init__(self):
        # Ex:
        # Insert(1)
        # Insert(2)
        # Insert(3)

        # self.ind = {1:0, 2:1, 3:2}
        # self.values = [1,2,3]

        self.ind = {}
        self.values = []
        
    def insert(self, val):
        # Approach 1:
        # - If val is in self.ind, then return False.
        # - Append val to values.
        # - Update self.ind for val such that it's index is the value, where val is the key!

        # TRICK: The correct test here is 'in'.
        if val in self.ind:
            return False
        
        self.values.append(val)
        self.ind[val] = len(self.values)-1
        # TRICK: Have to return true here.
        return True
        
    def remove(self, val):
        # Approach 1:
        # - If val is not in self.ind, then return False.
        # - Get the index i for val.
        # - Set the index of the last entry in values to have index i.
        # - Set the value of the entry in the list at index i to be the last entry.
        # - Delete the entry for val in the indices dictionary; delete the last value from the list.

        # TRICK: The correct test here is 'not in'.
        if val not in self.ind:
            return False
        
        i = self.ind[val]
        self.ind[self.values[-1]] = i
        self.values[i] = self.values[-1]

        self.ind.pop(val)
        self.values.pop()
        return True
        
    def getRandom(self):
        # Approach 1: Use the function 'random.choice(...)'.

        return random.choice(self.values)
        
# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
