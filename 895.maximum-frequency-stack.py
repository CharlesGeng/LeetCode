#
# @lc app=leetcode id=895 lang=python3
#
# [895] Maximum Frequency Stack
#

# @lc code=start
class FreqStack:
    def __init__(self):
        self.maxFreq = 0
        self.counter = collections.Counter()
        self.freqList = collections.defaultdict(list)

    def push(self, x: int) -> None:
        self.counter[x] += 1
        if self.maxFreq < self.counter[x]:
            self.maxFreq = self.counter[x]
        self.freqList[self.counter[x]].append(x)

    def pop(self) -> int:
        x = self.freqList[self.maxFreq].pop()
        if len(self.freqList[self.maxFreq]) == 0:
            self.maxFreq -= 1
        self.counter[x] -= 1
        return x


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
# @lc code=end
