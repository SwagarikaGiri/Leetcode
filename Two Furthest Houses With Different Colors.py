# There are n houses evenly lined up on the street, and each house is beautifully painted. You are given a 0-indexed integer array colors of length n, where colors[i] represents the color of the ith house.

# Return the maximum distance between two houses with different colors.

# The distance between the ith and jth houses is abs(i - j), where abs(x) is the absolute value of x.


from typing import List
class Solution:
    def maxDistance(self, colors: List[int]) -> int:
        colorDict=dict()
        for i in range(0,len(colors)):
            ele =colors[i]
            if(ele in colorDict):
                colorDict[ele].append(i)
            else:
                colorDict[ele]=[i]
        print(colorDict)
        key_iterable = colorDict.keys()
        list_index = list(key_iterable)
        maxDiff =float('-inf')
        for i in range(0,len(list_index)):
            for j in range (i+1,len(list_index)):
                col1 = list_index[i]
                col2 = list_index[j]
                a= min(colorDict[col1])
                b = max(colorDict[col1])
                c= min(colorDict[col2])
                d= max(colorDict[col2])
                diff = max(abs(d-a),abs(b-c))
                if(diff>maxDiff):
                    maxDiff=diff
        return maxDiff
                



sol = Solution()
sol.maxDistance([1,1,1,6,1,1,1])