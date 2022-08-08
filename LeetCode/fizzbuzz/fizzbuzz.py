class Solution(object):
    def fizzBuzz(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        n_list = []
        for x in range(1, n + 1):
            if x % 3 == 0 and x % 5 == 0:
                n_list.append('FizzBuzz')
            elif x % 3 == 0:
                n_list.append('Fizz')
            elif x % 5 == 0:
                n_list.append('Buzz')
            else:
                n_list.append(str(x))
        return n_list
