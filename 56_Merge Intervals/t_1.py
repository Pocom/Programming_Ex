class Solution:
    def merge(self, intervals):
        intervals.sort(key=lambda x: x[0])  # 以左侧边界排序

        merged = []
        for interval in intervals:
            if not merged or merged[-1][1] < interval[0]:  # 如果合并区间为空 或者 合并区间最后一个的右边界小于新加入的区间的左边界则加入新区间
                merged.append(interval)
            else:
                merged[-1][1] = max(merged[-1][1], interval[1])  # 如果新加入的区间的左边界小于或等于合并区间最后一个区间的右侧，则取两者右边界更大的一个

        return merged
