class Solution:
    def countAndSay(self, n: int) -> str:
        # 1 -> 11 -> 21 -> 1211 -> 111221 -> 312211
        start, tmp, count = ['1'], [], 1
        for i in range(n - 1):
            newLine = ''
            for seq, item in enumerate(start[i]):
                print('seq = {}, item = {}'.format(seq, item))
                tmp.append(item)

                print("tmp = {}, count = {}".format(tmp, count))
                if tmp.__len__() >= 2:
                    if tmp[-1] != tmp[-2]:
                        newLine += str(count) + tmp[-2]
                        print('newLine += ', newLine)
                        tmp = tmp[-1:]
                        count = 0
                    elif tmp[-1] == tmp[-2] and seq == len(start[i]) - 1:
                        if tmp.__len__() != len(start[i]):
                            count += 1
                        newLine += str(count) + tmp[-1]
                        print('newLine += ', newLine)
                        tmp.clear()
                        count = 0
                        break

                    if seq == len(start[i]) - 1:
                        newLine += str(1) + tmp[-1]
                        print('newLine += ', newLine)
                        tmp.clear()
                        count = 0
                        break
                elif seq == len(start[i]) - 1:
                    newLine += str(1) + tmp[-1]
                    print('newLine += ', newLine)
                    tmp.clear()
                    count = 0
                count += 1
            print('start = {}, newLine[{}] = {}'.format(start, i, newLine))
            start.append(newLine)
            print("\t")
        return start[n-1]


t = Solution()
print(t.countAndSay(7))
