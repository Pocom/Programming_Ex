class Solution(object):
    def reverse(self, x):
        x_list = list(str(x))
        res_stack = []
        is_minus = False  # 用于处理负数

        while x_list:
            v = x_list.pop()
            if v == '-':
                is_minus = True
                continue
            res_stack.append(v)
        res = int(''.join(res_stack))

        if is_minus:
            res *= -1

        # 边界条件
        v_max = 0xffffffff / 2
        if res > (v_max - 1) or res < (v_max * (-1)):
            res = 0

        return res
