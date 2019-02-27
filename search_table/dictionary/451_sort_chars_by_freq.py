from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        # solution 1
        # counter = Counter(s)
        # buckets = [''] * len(s)
        # for word, count in counter.items():
        #     buckets[count - 1] += word * count
        # buckets.reverse()
        # return ''.join(buckets)

        # solution 2
        # return ''.join(char * times for char, times in Counter(s).most_common())

        # solution 1
        counter = Counter(s)
        buckets = [None] * len(s)
        for word, count in counter.items():
            if not buckets[count - 1]:
                buckets[count - 1] = []
            buckets[count - 1].append(word * count)
        buckets.reverse()
        return ''.join(''.join(bucket) for bucket in buckets if bucket)


def test_solution():
    s = 'abbccc'
    assert Solution().frequencySort(s) == 'cccbba'
