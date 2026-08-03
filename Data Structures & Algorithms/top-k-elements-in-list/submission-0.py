class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        topDict = {}
        result = []
        for num in nums:
            if num not in topDict:
                topDict[num] = 1
            else:
                topDict[num] += 1

        pairs = list(topDict.items())
        pairs.sort(key=lambda x: x[1], reverse=True)

        for i in range(k):
            result.append(pairs[i][0])
        return result
            
            

        