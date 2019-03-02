# class MyHashSet:
#
#     def __init__(self):
#         """
#         Initialize your data structure here.
#         """
#         self.buckets = [False] * 1000000
#
#     def add(self, key: int) -> None:
#         self.buckets[key] = True
#
#     def remove(self, key: int) -> None:
#         self.buckets[key] = False
#
#     def contains(self, key: int) -> bool:
#         """
#         Returns true if this set contains the specified element
#         """
#         return self.buckets[key]

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = [None] * 1000

    def add(self, key: int) -> None:
        k = key % 1000
        if self.buckets[k] is None:
            self.buckets[k] = [False] * 1001
        self.buckets[k][key // 1000] = True

    def remove(self, key: int) -> None:
        k = key % 1000
        if self.buckets[k] is None:
            return
        self.buckets[k][key // 1000] = False

    def contains(self, key: int) -> bool:
        """
        Returns true if this set contains the specified element
        """
        k = key % 1000
        if self.buckets[k] is None:
            return False
        return self.buckets[k][key // 1000]


def test_solution():
    hset = MyHashSet()
    hset.add(1)
    hset.add(2)
    assert hset.contains(1)
    assert not hset.contains(3)
    hset.add(2)
    assert hset.contains(2)
    hset.remove(2)
    assert not hset.contains(2)
