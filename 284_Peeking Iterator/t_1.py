# Below is the interface for Iterator, which is already defined for you.
#
class Iterator:
    def __init__(self, nums):
        """
        Initializes an iterator object to the beginning of a list.
        :type nums: List[int]
        """

    def hasNext(self):
        """
        Returns true if the iteration has more elements.
        :rtype: bool
        """

    def next(self):
        """
        Returns the next element in the iteration.
        :rtype: int
        """


class PeekingIterator:
    def __init__(self, iterator):
        """
        Initialize your data structure here.
        :type iterator: Iterator
        """
        self.I_iter = iterator
        self.prev = None

    def peek(self):
        """
        Returns the next element in the iteration without advancing the iterator.
        :rtype: int
        """
        if self.prev:  # 如果前一个数存在 则输出
            return self.prev
        else:  # 如果前一个数不存在 则取出下一个数 迭代器后移
            nxt_num = self.I_iter.next()
            self.prev = nxt_num
            return nxt_num

    def next(self):
        """
        :rtype: int
        """
        if self.prev:  # 如果前一个数存在 则输出并设为 None
            num = self.prev
            self.prev = None
            return num
        else:
            return self.I_iter.next()

    def hasNext(self):
        """
        :rtype: bool
        """
        if self.prev:  # 如果前一个数存在 即使此时迭代器已经取完 但是该数还没被 next() 故返回 True
            return True
        if self.I_iter.hasNext():  # 如果 hasNext()
            return True
        return False


# Your PeekingIterator object will be instantiated and called as such:
nums = [1, 2, 3]
iter = PeekingIterator(Iterator(nums))
while iter.hasNext():
    val = iter.peek()  # Get the next element but not advance the iterator.
    iter.next()  # Should return the same value as [val].
