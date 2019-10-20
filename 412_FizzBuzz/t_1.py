class Solution:
    def fizzBuzz(self, n):
        """
        :param n: int
        :return: List[str]
        """
        ret = []
        for i in range(1, n+1):
            if i % 15 == 0: ret.append('FizzBuzz')
            elif i % 3 == 0: ret.append('Fizz')
            elif i % 5 == 0: ret.append('Buzz')
            else: ret.append(str(i))
        return ret

    def fizzBuzz2(self, n):
        """
        :param n: int
        :return: List[str]
        """
        multiples_3 = 3
        multiples_5 = 5
        ret = []
        for i in range(1, n + 1):
            if multiples_3 == i and multiples_5 == i:
                ret.append('FizzBuzz')
                multiples_3 += 3
                multiples_5 += 5
            elif multiples_3 == i:
                ret.append('Fizz')
                multiples_3 += 3
            elif multiples_5 == i:
                ret.append('Buzz')
                multiples_5 += 5
            else:
                ret.append(str(i))
        return ret
