class Solution:
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        for x in range(1, n+1):
            if x % 3 == 0 and x % 5 == 0:
                ans.append('FizzBuzz')
            elif x % 3 == 0:
                ans.append('Fizz')
            elif x % 5 == 0:
                ans.append('Buzz')
            else:
                ans.append(str(x))
        return ans


def test_solution():
    n = 15
    res = [
        '1',
        '2',
        'Fizz',
        '4',
        'Buzz',
        'Fizz',
        '7',
        '8',
        'Fizz',
        'Buzz',
        '11',
        'Fizz',
        '13',
        '14',
        'FizzBuzz'
    ]
    assert Solution().fizzBuzz(n) == res
