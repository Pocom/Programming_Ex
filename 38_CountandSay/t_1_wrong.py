class Solution:
    def countAndSay(self, n: int) -> str:  # interpretive error
        # 1 -> 11 -> 21 -> 1211 -> 111221 -> 2111121211
        dict_ = {'1': '11', '11': '21', '2': '12'}
        start = ['1']
        tmp = []
        for i in range(n):
            newLine = ''
            for seq, item in enumerate(start[i]):
                print(seq, item)
                tmp.append(item)
                if len(tmp) == 2:
                    print('tmp has two elements.')
                    if "".join(tmp) in dict_:
                        print('dict_ has corresponding two elements.')
                        newLine += dict_[''.join(tmp)]
                        tmp.clear()
                    else:
                        print('dict_ has corresponding one elements.')
                        newLine += dict_[tmp.pop(0)]
                        if seq == len(start[i]) - 1:
                            newLine += dict_[''.join(tmp)]
                            tmp.clear()
                elif seq == len(start[i]) - 1:
                    print('its last one')
                    newLine += dict_[''.join(tmp)]
                    tmp.clear()
            print('newLine = ', newLine)
            start.append(newLine)
            print('\t')
        return start[n-1]


t = Solution()
print(t.countAndSay(4))
