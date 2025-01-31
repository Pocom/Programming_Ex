from typing import List


class Solution:
    directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]

    def exist(self, board: List[List[str]], word: str) -> bool:
        m = len(board)
        if m == 0: return False
        n = len(board[0])

        marked = [[False for _ in range(n)] for _ in range(m)]  # 记录访问过的位置
        for i in range(m):
            for j in range(n):
                # 对每一个格子都从头开始搜索
                if self.__search_word(board, word, 0, i, j, marked, m, n):
                    return True
        return False

    def __search_word(self, board, word, index, start_x, start_y, marked, m, n):
        # 二维平面 单词 当前查询字母的索引 当前查询平面的索引 访问过记录 二维平面的宽高
        if index == len(word) - 1: return board[start_x][start_y] == word[index]  # 最后一个单词的时候来判定是否是一致 从而递归结束

        # 中间匹配了，再继续搜索
        if board[start_x][start_y] == word[index]:
            # 先占住这个位置，搜索不成功的话，要释放掉
            marked[start_x][start_y] = True
            for direction in self.directions:
                new_x = start_x + direction[0]
                new_y = start_y + direction[1]
                # 注意：如果这一次 search word 成功的话，就返回
                if 0 <= new_x < m and 0 <= new_y < n and not marked[new_x][new_y] and \
                        self.__search_word(board, word, index + 1, new_x, new_y, marked, m, n):
                    return True
            marked[start_x][start_y] = False
        return False
