class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        ret = 0
        for i in range(32):
            ret <<= 1  # 向左移一位
            ret += n & 1  # 最左位与 1 进行与运算
            n >>= 1  # 向右移一位
        return ret
