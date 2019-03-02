class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.buckets = [None] * 1000

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        k = key % 1000
        if self.buckets[k] is None:
            self.buckets[k] = [-1] * 1001
        self.buckets[k][key // 1000] = value

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        k = key % 1000
        if self.buckets[k] is None:
            return -1
        return self.buckets[k][key // 1000]

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        k = key % 1000
        if self.buckets[k] is None:
            return
        self.buckets[k][key // 1000] = -1


def test_solution():
    hmap = MyHashMap()
    hmap.put(1, 1)
    hmap.put(2, 2)
    assert hmap.get(1) == 1
    assert hmap.get(3) == -1
    hmap.put(2, 1)
    assert hmap.get(2) == 1
    hmap.remove(2)
    assert hmap.get(2) == -1
