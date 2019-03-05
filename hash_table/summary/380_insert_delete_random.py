import random


class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = []
        self.hmap = {}

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.hmap:
            return False
        self.hmap[val] = len(self.nums)
        self.nums.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val not in self.hmap:
            return False

        n, index = len(self.nums), self.hmap[val]
        if index < n - 1:
            last = self.nums[n - 1]
            self.nums[index] = last
            self.hmap[last] = index

        self.nums.pop()
        del self.hmap[val]

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        return self.nums[random.randint(0, len(self.nums) - 1)]


# class RandomizedSet:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.nums = []
#         self.hmap = {}
#         self.empty_seats = []
#
#     def insert(self, val: int) -> bool:
#         """
#         Inserts a value to the set. Returns true if the set did not already contain the specified element.
#         """
#         if val in self.hmap:
#             return False
#         if len(self.empty_seats) == 0:
#             key = len(self.nums)
#             self.hmap[val] = key
#             self.nums.append(val)
#         else:
#             key = self.empty_seats.pop()
#             self.hmap[val] = key
#             self.nums[key] = val
#         return True
#
#     def remove(self, val: int) -> bool:
#         """
#         Removes a value from the set. Returns true if the set contained the specified element.
#         """
#         if val not in self.hmap:
#             return False
#         key = self.hmap[val]
#         del self.hmap[val]
#         self.nums[key] = -1
#         self.empty_seats.append(key)
#         return True
#
#     def getRandom(self) -> int:
#         """
#         Get a random element from the set.
#         """
#         if len(self.hmap) == 0:
#             return -1
#         n = len(self.nums)
#         while True:
#             i = random.randint(0, n - 1)
#             if self.nums[i] != -1:
#                 return self.nums[i]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

def test_solution():
    s = RandomizedSet()
    assert s.insert(1)
    assert not s.remove(2)
    assert s.insert(2)
    assert s.getRandom()
    assert s.remove(1)
    assert not s.insert(2)
