class Solution:
    def countAndSay(self, n: int) -> str:
        if n <= 1:
            return '1'
        ans = '1'  # 当前最新计算出的报数
        # repeat 当前被重复数字的重复次数
        # p 当前被重复的数字
        for i in range(1, n):
            last_ans = ans
            ans = ""
            p = last_ans[0]
            repeat = 0
            for j in range(len(last_ans)):
                if last_ans[j] == p:
                    repeat += 1
                else:
                    ans = ans+str(repeat)+p
                    p = last_ans[j]
                    repeat = 1
            ans = ans+str(repeat)+p
        return ans
