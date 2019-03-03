class Solution:
    def findRestaurant(self, list1: 'List[str]', list2: 'List[str]') -> 'List[str]':
        ans, hmap = [], dict()
        for i, rest in enumerate(list1):
            hmap[rest] = [i]

        min_sum = (len(list1) - 1) + (len(list2) - 1)
        for j, rest in enumerate(list2):
            if rest in hmap:
                hmap[rest].append(j)
                idx_sum = hmap[rest][0] + hmap[rest][1]
                if idx_sum == min_sum:
                    ans.append(rest)
                elif idx_sum < min_sum:
                    min_sum = idx_sum
                    ans.clear()
                    ans.append(rest)
        return ans


def test_solution():
    list1 = ['Shogun', 'Tapioca Express', 'Burger King', 'KFC']
    list2 = ['Piatti', 'The Grill at Torrey Pines', 'Hungry Hunter Steakhouse', 'Shogun']
    assert Solution().findRestaurant(list1, list2) == ['Shogun']

    list1 = ['Shogun', 'Tapioca Express', 'Burger King', 'KFC']
    list2 = ["KFC", "Shogun", "Burger King"]
    assert Solution().findRestaurant(list1, list2) == ['Shogun']
