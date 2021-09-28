#
# @lc app=leetcode id=68 lang=python3
#
# [68] Text Justification
#

# @lc code=start
class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        result = []
        line = ""
        for word in words:
            if len(line) + len(word) <= maxWidth:
                line += word + " "
            else:
                newLine = line.rstrip()
                spacesCount = maxWidth - len(newLine)
                words = newLine.split(" ")
                if len(words) == 1:
                    newLine = words[0] + " " * spacesCount
                else:
                    spaces = [" "] * (len(words) - 1)
                    i = 0
                    while spacesCount > 0:
                        spaces[i] += " "
                        i += 1
                        spacesCount -= 1
                        if i == len(spaces):
                            i = 0
                    newPairs = zip(words, spaces)
                    newLine = ""
                    for i in newPairs:
                        newLine += i[0] + i[1]
                    newLine += words[-1]
                result.append(newLine)
                line = word + " "
        line = line.rstrip()
        result.append(line + " " * (maxWidth - len(line)))
        return result


# @lc code=end
